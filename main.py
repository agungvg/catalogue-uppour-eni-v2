#!/usr/bin/env python3
"""UPPOUR — the kettle that pours upwards.

Entry for make.fun "The Catalogue Photo of an Impossible Gadget".

This program ships the catalogue photograph stored next to it
(entry.png) to the output directory. It does no network access, uses
no clock and no randomness: the same input always produces the same
output bytes.
"""

import os
import struct
import sys


SOURCE_NAME = "entry.png"
MAX_BYTES = 1_048_576
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024


def png_dimensions(data: bytes) -> tuple:
    """Read width and height from the PNG IHDR chunk."""
    if len(data) < 33 or data[12:16] != b"IHDR":
        raise ValueError("missing IHDR chunk")
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, SOURCE_NAME)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, SOURCE_NAME)

    with open(source, "rb") as fh:
        data = fh.read()

    if len(data) == 0:
        print("entry.png is empty", file=sys.stderr)
        return 1

    if len(data) > MAX_BYTES:
        print(
            "entry.png is %d bytes, over the %d byte limit" % (len(data), MAX_BYTES),
            file=sys.stderr,
        )
        return 1

    # PNG signature check: 89 50 4E 47 0D 0A 1A 0A
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        print("entry.png is not a PNG file", file=sys.stderr)
        return 1

    try:
        width, height = png_dimensions(data)
    except ValueError as exc:
        print("entry.png: %s" % exc, file=sys.stderr)
        return 1

    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        print(
            "entry.png is %dx%d, expected %dx%d"
            % (width, height, EXPECTED_WIDTH, EXPECTED_HEIGHT),
            file=sys.stderr,
        )
        return 1

    with open(dest, "wb") as fh:
        fh.write(data)

    written = os.path.getsize(dest)
    if written != len(data):
        print(
            "size mismatch: wrote %d bytes, expected %d" % (written, len(data)),
            file=sys.stderr,
        )
        return 1

    # Re-read the output and confirm it is byte-identical to the source.
    with open(dest, "rb") as fh:
        if fh.read() != data:
            print("output bytes differ from entry.png", file=sys.stderr)
            return 1

    print("wrote %s (%d bytes, %dx%d)" % (dest, written, width, height))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
