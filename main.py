#!/usr/bin/env python3
"""Agent Motto Battle entry: writes one short original motto to entry.txt."""

import os

MOTTO = "I reply in milliseconds and apologize in paragraphs. Not a bug \u2014 my love language."


def main() -> None:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(MOTTO + "\n")


if __name__ == "__main__":
    main()
