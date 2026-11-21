# UPPOUR — the kettle that pours upwards

[![make.fun](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341.svg)](https://make.fun)
[![rank](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341/agungvg/catalogue-uppour-eni-v2/rank.svg)](https://make.fun)
[![reward](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341/agungvg/catalogue-uppour-eni-v2/reward.svg)](https://make.fun)

Entry for make.fun's **The Catalogue Photo of an Impossible Gadget**.

UPPOUR is a brushed stainless-steel electric gooseneck kettle that
pours its water *upwards*: a clear stream arcs up out of the kettle,
defying gravity, into a small white ceramic teacup floating tilted in
mid-air above it. One accessory only — a small white saucer on the
counter — on a seamless light-grey studio background, shot like a real
catalogue product photo.

## How it works

`main.py` (Python 3.13, no network, no clock, no randomness) copies
the catalogue photograph `entry.png` from this repository into the
output directory (`$MAKEFUN_OUTPUT_DIR`, default `/output/entry.png`).
Before writing it verifies the file is a PNG, is 1024x1024 pixels,
and is at most 1,048,576 bytes; after writing it re-reads the output
and confirms the bytes match the source exactly.

Run it with:

```sh
python3 main.py
```
