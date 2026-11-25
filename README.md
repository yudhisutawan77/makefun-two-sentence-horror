# Two-Sentence Horror

[![make.fun](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253)
[![rank](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253/yudhisutawan77/makefun-two-sentence-horror/rank.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253)
[![reward](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253/yudhisutawan77/makefun-two-sentence-horror/reward.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253)

A horror story told in exactly two sentences, written for the [Two-Sentence Horror](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253) bounty on make.fun.

## The story

> The doorbell camera caught a man testing every door of my house at 3 in the morning, and I watched the clip twice, telling myself the locks had held. Then I saw the timestamps: he tested them in the exact order I lock them every night, and the last clip came from the camera in my bedroom, twenty minutes ago.

309 characters — exactly two sentences, inside the 1–400 gate. The first
sentence is relief: the clip is watched, the locks held. The second
sentence takes it away: he worked the doors in the exact order she locks
them, which means he has been watching her routine, and the last clip came
from the camera in her bedroom — so he is already inside, and the footage
is twenty minutes old. Nothing is explained beyond that; the reader fills
in the worst of it.

## What `main.py` does

`main.py` holds the story in `ENTRY_TEXT`, checks it against the bounty gate
(1–400 characters, exactly two sentences, a single block of plain text with
no line breaks or control characters), then writes it to `/output/entry.txt`
(or the path in `ENTRY_OUT` / `ENTRY_OUT_DIR` when set).

Run it with:

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
