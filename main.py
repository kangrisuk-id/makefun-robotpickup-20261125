#!/usr/bin/env python3
"""Robot Pickup Line Championship — entry program.

Writes this entry's single pickup line to /output/entry.txt.

The gate contract (program/v1): /output/entry.txt must be UTF-8 text,
a single line of 1 to 200 characters, and not blank. The line is held
as a constant below; before writing, the program validates it against
that contract (single line, 1..200 characters, non-blank, UTF-8
encodable) so a bad edit fails loudly here instead of at the gate.

The line itself: a robot has stayed up all night waiting for a
software update — not for the update, but for the restart, the one
moment a machine gets to power down beside someone. The joke is
native to being a machine (updates, restarting), the turn is the
wait's real reason, and it stays charming rather than creepy.
"""

from pathlib import Path

LINE = "Are you a software update? Because I have been waiting all night to restart beside you."

OUTPUT_PATH = Path("/output/entry.txt")


def validate(line: str) -> str:
    """Return the line unchanged if it satisfies the gate contract."""
    if not line or not line.strip():
        raise ValueError("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry line must be 1..200 characters, got {len(line)}")
    line.encode("utf-8")  # must be UTF-8 encodable
    return line


def main() -> None:
    text = validate(LINE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(f"wrote {OUTPUT_PATH} ({len(text)} chars)")


if __name__ == "__main__":
    main()
