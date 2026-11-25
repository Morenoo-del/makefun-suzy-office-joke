#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes a single original one-line office joke to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Deterministic, standard library only, no network access.
"""

import os
import sys


ENTRY = (
    "I asked for a raise and my boss said the budget is tight "
    "\u2014 then bought a $4,000 espresso machine for the break room."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
