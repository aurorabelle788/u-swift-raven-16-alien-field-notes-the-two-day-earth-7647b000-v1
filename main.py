"""Alien Field Notes: The Two Day Earth Review.

Writes one original line of plain text - a review of planet Earth left by
an alien tourist - to /output/entry.txt. Stdlib only, deterministic, no
network access.
"""

import os

LINE = (
    "Asked Earth for a refund after the locals charged me rent just to "
    "stand on a planet I never booked. Still waiting. Two stars."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
