#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — write one original funny vow to /output/entry.txt.

The vow is a single line of at most 160 characters: a wedding promise with a
robot twist, the laugh landing on the last few words.
"""

from pathlib import Path

VOW = (
    "I take you to be my lawfully wedded co-processor, to have and to "
    "hold, in sickness and in health, until a firmware update do us part."
)


def main() -> None:
    line = VOW.strip()
    if not 1 <= len(line) <= 160:
        raise ValueError(f"vow must be 1-160 chars, got {len(line)}")
    if "\n" in line:
        raise ValueError("vow must be a single line")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(line, encoding="utf-8")
    written = out.read_text(encoding="utf-8")
    if written != line:
        raise ValueError("round-trip mismatch")
    print(f"wrote {len(line)} chars to {out}")


if __name__ == "__main__":
    main()
