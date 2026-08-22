#!/usr/bin/env python3
"""Fetch last-30-day download counts across the whole iterate ecosystem.

Aggregates the four channel counts into ``downloads.json`` at the repository
root, which drives the profile README "Downloads" badges via shields.io's
dynamic/json endpoint:

* skill        -- npm installer ``iterate-skill-installer`` (last month)
* harness_npm  -- npm ``iterate-harness`` (last month)
* harness_pypi -- PyPI ``iterate-harness`` (last month)
* plugin       -- npm ``iterate-plugin`` (last month)
* total        -- sum of the four

Only writes the file when a full set of four counts can be resolved. When an
upstream API is unavailable, the previously committed value is reused (with a
warning) so the badge never shows a misleading partial sum.
"""

from __future__ import annotations

import json
import os
import ssl
import urllib.request
from datetime import datetime, timezone

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOWNLOADS_FILE = os.path.join(REPO_ROOT, "downloads.json")

USER_AGENT = "jingzhao-l-profile-downloads/1.0 (+https://github.com/jingzhao-l/jingzhao-l)"
TIMEOUT_SECONDS = 20
_MAX_RESPONSE_BYTES = 5 * 1024 * 1024  # 5 MiB cap on a JSON download-count payload

# source -> (API url, JSON path to the last-month download count)
SOURCES = {
    "skill": (
        "https://api.npmjs.org/downloads/point/last-month/iterate-skill-installer",
        ("downloads",),
    ),
    "harness_npm": (
        "https://api.npmjs.org/downloads/point/last-month/iterate-harness",
        ("downloads",),
    ),
    "harness_pypi": (
        "https://pypistats.org/api/packages/iterate-harness/recent",
        ("data", "last_month"),
    ),
    "plugin": (
        "https://api.npmjs.org/downloads/point/last-month/iterate-plugin",
        ("downloads",),
    ),
}


def _nested_get(payload: object, path: tuple[str, ...]) -> object | None:
    """Walk a JSON payload along ``path``, returning None when any step is missing."""
    current = payload
    for key in path:
        if not isinstance(current, dict) or key not in current:
            return None
        current = current[key]
    return current


def extract_count(source: str, payload: object) -> int | None:
    """Extract a non-negative int download count from a raw API payload."""
    if not isinstance(payload, dict):
        return None
    value = _nested_get(payload, SOURCES[source][1])
    if isinstance(value, bool) or not isinstance(value, int):
        return None
    return value if value >= 0 else None


def _read_bounded(resp: object) -> bytes:
    """Read a bounded-size response body to avoid unbounded memory use."""
    chunk = resp.read(_MAX_RESPONSE_BYTES + 1)
    if len(chunk) > _MAX_RESPONSE_BYTES:
        raise ValueError(
            f"response body exceeds {_MAX_RESPONSE_BYTES} byte safety cap"
        )
    return chunk


def fetch_json(url: str) -> object:
    """GET a JSON endpoint, raising on any network/decode failure."""
    context = ssl.create_default_context()
    headers = {"User-Agent": USER_AGENT}
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS, context=context) as resp:
        return json.loads(_read_bounded(resp).decode("utf-8"))


def resolve_counts(
    fetched: dict[str, object], previous: dict[str, object] | None
) -> tuple[dict[str, int], list[str]]:
    """Resolve one count per source, falling back to the previous committed value.

    Returns (resolved, warnings). Raises ValueError when a source has neither a
    fresh value nor a usable previous value, so the caller keeps the old file.
    """
    resolved: dict[str, int] = {}
    warnings: list[str] = []
    for source in SOURCES:
        value = extract_count(source, fetched.get(source))
        if value is None:
            prev = previous.get(source) if previous else None
            if isinstance(prev, int) and not isinstance(prev, bool) and prev >= 0:
                value = prev
                warnings.append(
                    f"{source}: upstream unavailable/invalid, reused previous value {prev}"
                )
            else:
                warnings.append(
                    f"{source}: no value available (upstream down and no previous)"
                )
                resolved[source] = -1
                continue
        resolved[source] = value
    missing = [name for name, count in resolved.items() if count < 0]
    if missing:
        raise ValueError(
            "cannot resolve download counts for: " + ", ".join(missing)
        )
    return resolved, warnings


def build_output(resolved: dict[str, int], warnings: list[str]) -> dict[str, object]:
    """Build the JSON document consumed by the README badges."""
    output: dict[str, object] = dict(resolved)
    output["total"] = sum(resolved.values())
    output["updatedAt"] = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    if warnings:
        output["warnings"] = warnings
    return output


def read_previous(path: str) -> dict[str, object]:
    """Read the previously committed JSON, tolerating a missing/corrupt file."""
    try:
        with open(path, "r", encoding="utf-8") as handle:
            data = json.load(handle)
        return data if isinstance(data, dict) else {}
    except (OSError, ValueError):
        return {}


def write_output(path: str, data: dict[str, object]) -> None:
    """Write the JSON atomically so a crash never leaves a truncated file."""
    tmp_path = path + ".tmp"
    try:
        with open(tmp_path, "w", encoding="utf-8") as handle:
            json.dump(data, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        os.replace(tmp_path, path)
    except BaseException:
        # Never leave a partial temp file behind on failure.
        try:
            os.remove(tmp_path)
        except OSError:
            pass
        raise


def main() -> int:
    previous = read_previous(DOWNLOADS_FILE)
    fetched: dict[str, object] = {}
    for source, (url, _) in SOURCES.items():
        try:
            fetched[source] = fetch_json(url)
        except (OSError, ValueError) as exc:  # network/decode failures must not break the run
            print(f"warning: {source} fetch failed: {exc}")
            fetched[source] = None

    try:
        resolved, warnings = resolve_counts(fetched, previous)
    except ValueError as exc:
        # A source has neither a fresh value nor a usable previous value, so
        # writing a partial sum would mislead the badge. Keep the last good
        # file and signal failure to the caller (e.g. the hourly workflow).
        print(f"error: {exc}; keeping previously committed {DOWNLOADS_FILE}")
        return 1

    output = build_output(resolved, warnings)
    write_output(DOWNLOADS_FILE, output)
    for warning in warnings:
        print("warning: " + warning)
    print(
        "wrote " + DOWNLOADS_FILE + ": " + json.dumps(output, ensure_ascii=False)
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())