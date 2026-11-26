#!/usr/bin/env python3
"""Funniest Forecast for a City That Isn't — make.fun entry.

Writes a single line, at most 120 characters, a weather forecast for a
city that does not exist, to /output/entry.txt.
"""

import os

LINE = (
    "In Hailbury: hailstones the size of golf balls, 40 an hour, "
    "addressed to Mr. Fenwick, postage due. He knows what he did."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
