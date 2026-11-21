#!/usr/bin/env python3
"""Copy the pre-rendered entry.png to the output directory.

The front page is rendered offline (the sandbox has no network), so this
program only copies bytes: both runs write identical output.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    src = os.path.join(HERE, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    if os.path.getsize(src) != os.path.getsize(dst):
        raise SystemExit("entry.png copy size mismatch")
    return 0


if __name__ == "__main__":
    sys.exit(main())
