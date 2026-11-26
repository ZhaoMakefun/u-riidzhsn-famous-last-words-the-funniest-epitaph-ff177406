#!/usr/bin/env python3
# Famous Last Words: The Funniest Epitaph.
# The epitaph: a man who at last finished his to-do list, only to
# discover the final item was "die" — and, being thorough to the
# end, he checked it off anyway. Productivity, taken to its grave.
# Validation below enforces the 150-character, single-line rule.

import os
import sys

EPITAPH = "Here lies a man who finally finished his to-do list — turns out the last item was 'die.' He checked it off anyway."
CHAR_LIMIT = 150


def produce():
    wording = EPITAPH.strip()
    if wording == "":
        print("epitaph rejected: nothing to write", file=sys.stderr)
        return 1
    if len(wording) > CHAR_LIMIT:
        print(
            f"epitaph rejected: {len(wording)} characters exceeds {CHAR_LIMIT}",
            file=sys.stderr,
        )
        return 1
    if "\n" in wording or "\r" in wording:
        print("epitaph rejected: line breaks are not allowed", file=sys.stderr)
        return 1
    wording.encode("utf-8")
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(folder, exist_ok=True)
    destination = os.path.join(folder, "entry.txt")
    with open(destination, "w", encoding="utf-8") as stream:
        stream.write(wording)
    return 0


sys.exit(produce())
