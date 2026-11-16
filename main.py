#!/usr/bin/env python3
"""ai-excited-01: copy entry.png to the output directory.

Deterministic: the output is a byte-for-byte copy of entry.png,
so repeated runs produce identical bytes.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dst = out_dir / "entry.png"
    shutil.copyfile(SRC, dst)
    size = dst.stat().st_size
    print(f"Wrote {dst} ({size} bytes)")


if __name__ == "__main__":
    main()
