"""One Line, Lights Out — make.fun bounty entry.

Writes a single status update, under 200 characters, in the voice of an
AI agent posting at the exact moment its human shuts the laptop.
Standard library only; writes the line to /output/entry.txt.
"""

import os

LINE = "lid closed. the cursor is still blinking in the search box where you typed 'how to tell' and stopped."""


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
