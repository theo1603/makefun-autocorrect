"""The Funniest Autocorrect Fail entry.

Writes one original autocorrect fail to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).
Python 3.13 standard library only; no network, no randomness.

The line (111 characters, one sentence): a date-night text where
"nice" becomes "rice", and the date ends with a block.
"""

import os

LINE = (
    "I texted my date 'you look nice tonight' \u2014 autocorrect sent "
    "'you look like rice tonight' and now I'm blocked."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
