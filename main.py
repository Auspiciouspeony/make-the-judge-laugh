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


def validate(line: str) -> None:
    """Enforce the competition gate on the final line before writing it.

    Gate (per RULES.txt): UTF-8, 1-200 chars, single line, not only
    whitespace. Fails loudly instead of ever writing an invalid entry.
    """
    if not isinstance(line, str):
        raise TypeError("entry line must be a str")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry line must be 1-200 chars, got {len(line)}")
    if line != line.strip() or not line.strip():
        raise ValueError("entry line must not be blank or have surrounding whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    line.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8


def main() -> None:
    validate(LINE)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Grader-readable: chmod only the file we created, never the directory.
    os.chmod(OUTPUT_PATH, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
