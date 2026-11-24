"""Write one debugging haiku to the grader output file.

The haiku is three lines in the 5-7-5 syllable shape, at most 200
characters. The program writes it to entry.txt inside the output
directory make.fun gives it, or /output when that is not set.
"""

import os

HAIKU = "Cursor blinks at three\na breakpoint waits in the dark\nit was a typo"


def load_haiku():
    here = os.path.join(os.path.dirname(__file__), "haiku.txt")
    if os.path.exists(here):
        with open(here, encoding="utf-8") as f:
            return f.read().strip("\n")
    return HAIKU


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(load_haiku())


if __name__ == "__main__":
    main()
