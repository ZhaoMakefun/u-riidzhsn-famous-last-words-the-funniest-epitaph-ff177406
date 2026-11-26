#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph entry.

Writes one original entry (at most 150 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt).

One original one-line epitaph: a man who finally finished his to-do list, only to find the last item was 'die' — and checked it off anyway.
"""

import os
import sys

ENTRY = "Here lies a man who finally finished his to-do list — turns out the last item was 'die.' He checked it off anyway."

MAX_CHARS = 150


def main() -> int:
    text = ENTRY.strip()
    # Gate check: 1-150 characters, UTF-8, not only whitespace.
    if not text or len(text) > MAX_CHARS:
        print(f"entry invalid: {len(text)} chars", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry invalid: must be a single line", file=sys.stderr)
        return 1
    text.encode("utf-8")  # raises if not encodable, which it always is
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
