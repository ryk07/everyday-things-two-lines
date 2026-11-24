#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run.

A two-line explanation of one everyday thing for a 10-year-old.

Line 1 explains a traffic jam in a single vivid sentence built on
one analogy: a zipper stuck halfway. Line 2 says in one sentence
why that analogy works: what it maps (cars merging one by one,
like zipper teeth) and what it leaves out (the drivers, the red
lights, and why the road jammed at all).

The program writes exactly those two lines to /output/entry.txt,
the artifact the sealed scorer gates and the house judge compares.
Standard library only; no network, no file reads outside this
program, no working-directory assumptions.
"""

import os

# The entry: two lines, written here as the program's own data.
# Line one is a single vivid sentence with one concrete analogy;
# line two is one honest sentence about what the analogy maps
# and what it leaves out.
LINE_ONE = "A traffic jam is a zipper stuck halfway, its teeth cars jammed bumper to bumper with nowhere to slide."
LINE_TWO = "It maps how cars must merge one by one like teeth, but it leaves out the drivers, the red lights, and why the road jammed at all."

OUTPUT_DIR = "/output"
OUTPUT_NAME = "entry.txt"


def build_text():
    """Join the two lines with a single newline, no trailing newline."""
    return LINE_ONE + "\n" + LINE_TWO


def main():
    text = build_text()
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_path = os.path.join(OUTPUT_DIR, OUTPUT_NAME)
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
