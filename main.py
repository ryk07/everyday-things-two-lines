#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run.

A two-line entry about an everyday thing: the smoke detector whose
battery only ever dies in the middle of the night.

The program writes exactly two lines of original text to
/output/entry.txt, the artifact the sealed scorer gates and the
house judge compares. Standard library only; no network, no file
reads outside this program, no working-directory assumptions.
"""

import os

# The entry: two lines, written here as the program's own data.
# Line one sets up the everyday thing with a specific, odd detail;
# line two lands the twist with a fresh comparison.
LINE_ONE = "The smoke detector's battery only dies at 3 a.m. — never at 3 p.m."
LINE_TWO = "It waits until I am sound asleep, then chirps once, like a tiny landlord demanding rent."

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
