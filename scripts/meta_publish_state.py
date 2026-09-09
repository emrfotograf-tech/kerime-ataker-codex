#!/usr/bin/env python3
"""Safe runtime-state wrapper for the Kerime Ataker Meta publisher.

The publishing implementation remains in meta_publish.py. This wrapper points its
queue at a mutable state checkout and returns a non-zero exit status whenever a
processed item ends in partial_failed, while still allowing the workflow to
persist the updated state.
"""

import json
import os
from pathlib import Path

import meta_publish


def main() -> int:
    queue_dir = Path(os.getenv("META_PUBLISH_QUEUE_DIR", "publish_queue"))
    meta_publish.QUEUE_DIR = queue_dir

    code = meta_publish.main()
    if code:
        return code

    failed = []
    if queue_dir.exists():
        for path in sorted(queue_dir.glob("*.json")):
            try:
                item = json.loads(path.read_text(encoding="utf-8"))
            except Exception as exc:
                print(f"{path}: invalid queue JSON after publish: {exc}")
                failed.append(str(path))
                continue
            if item.get("status") == "partial_failed":
                failed.append(item.get("id") or path.name)

    if failed:
        print("Meta publishing failures persisted for: " + ", ".join(failed))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
