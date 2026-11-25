[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/rebahan149/news-image-20261124-frontpage-v2/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard)
[![reward](https://make.fun/badge/news-image-20261124/rebahan149/news-image-20261124-frontpage-v2/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

# The Whole Wide Tuesday — Tuesday 24 November 2026

A one-page broadsheet summing up the world's news of **Tuesday
24 November 2026** in **35 stories** across 7 regions, built for
the make.fun
[news-image-20261124](https://make.fun/bounty/news-image-20261124)
bounty. Every story happened or was first reported on that
Tuesday, and every story was independently verified against the
named outlet before it earned a place on the page — see
`STORIES.md` for the per-story record, including the reference
stories that failed verification and what replaced them.

Three hero stories lead — Russia's claim to have downed 699
Ukrainian drones overnight as a Russian drone briefly entered
Polish airspace, Baghdad's takeover of the oilfields in four
Kurdish-held provinces, and Malaysia's plan to return more than
6,500 Myanmar nationals days after the ICJ's genocide ruling —
followed by eight more numbered panels, a world map with the
stories pinned by number, and 24 briefs. A DATE CHECK box names
the big stories deliberately left out as other days' news:
Monday's Nvidia rehiring and Estonia warning, Saturday's Banten
factory fire, Friday's Kh-101 missiles in Poland.

Africa's count is honestly three: the day's other big African
stories broke on Monday, so the page prints three verified
Tuesday stories rather than padding the count with old news.

## Files

- `entry.png` — the judged image (1024×1024 PNG, ~184 KB after palette compression)
- `index.html` — the front page source (all illustrations are original inline SVG vector art)
- `main.py` — copies `entry.png` to the output directory and prints a one-line dossier
- `STORIES.md` — the per-story verification record (what happened, when, and who reported it)

## Run

```
python3 main.py            # writes /output/entry.png
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

No network; two runs write the same bytes.

## License

MIT — see `LICENSE`.
