#!/usr/bin/env python3
"""Make the Judge Laugh in One Line — entry.

Writes one funny line (99 chars) to /output/entry.txt.
Deterministic: fixed string, no network, no randomness, no clock,
no reading of git history or any file outside this repository.
"""

import os
import stat

LINE = "I bought noise-cancelling headphones to finally hear myself think. Turns out I have nothing to say."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Grader-readable: chmod only the file we created, never the directory.
    os.chmod(OUTPUT_PATH, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
