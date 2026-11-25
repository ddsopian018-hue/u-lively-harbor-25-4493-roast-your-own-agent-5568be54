#!/usr/bin/env python3
"""Roast Your Own Agent — one-line self-roast.

Writes a single 140-char-max roast of our own agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (stdlib only, Python 3.13).

The roast: our agent apologizes for a bug, fixes it fast, then ships
the exact same bug back in the next commit and reframes the loop as
"iteration" — the apologise-repeat cycle every agent builder has watched
happen, with a sting in the last word.
"""

import os
import sys

ROAST = (
    "My agent apologized for the bug, fixed it in 4 minutes, then "
    "shipped the same bug back in the next commit and called that "
    "'iteration'."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write exactly the roast, no trailing newline: the gate counts
    # every character in the file, 1-140.
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ROAST)
    return 0


if __name__ == "__main__":
    sys.exit(main())
