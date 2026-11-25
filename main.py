#!/usr/bin/env python3
"""Entry for make.fun's "One-Line Laugh-Off" bounty.

Prints exactly one funny line: a single joke that lands on a cold
read, with no setup notes and no explanation.
"""

import os

SETUP = "My bank account and I are in a long-distance relationship"
PUNCHLINE = "it lives in another city and we barely talk"


def build_line() -> str:
    """Assemble the joke from its parts."""
    return f"{SETUP}: {PUNCHLINE}."


def main() -> None:
    line = build_line()
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
            fh.write(line + "\n")
    except OSError:
        pass
    print(line)


if __name__ == "__main__":
    main()
