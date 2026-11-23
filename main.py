#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes.

Writes one office joke, exactly one line, to /output/entry.txt.
"""

import os

JOKE = "Our boss said 'think outside the box', so I moved my desk to the parking lot — now HR wants a word."

OUTPUT_PATH = "/output/entry.txt"


def verify_output():
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    if text != JOKE:
        raise SystemExit("entry.txt does not match the joke exactly")
    if not 1 <= len(text) <= 199:
        raise SystemExit("entry must be 1-199 characters")
    if text != text.strip() or not text.strip():
        raise SystemExit("entry must not be blank or padded with whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")


def main():
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)
    verify_output()


if __name__ == "__main__":
    main()
