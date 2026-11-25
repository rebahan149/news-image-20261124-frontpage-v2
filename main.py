# Entrypoint for the news-image-20261124 entry (v2 page).
# The judged artifact is entry.png (1024x1024 PNG, <= 1 MiB): one front
# page — masthead "The Whole Wide Tuesday" — summing up Tuesday
# 24 November 2026 in 35 stories across 7 regions — 3 illustrated
# hero panels, 8 more numbered panels, a pinned world map,
# 24 briefs and a date-check box.
# The page source is index.html; the per-story verification record is
# STORIES.md. This program copies entry.png into $MAKEFUN_OUTPUT_DIR
# (default /output) and prints a one-line dossier describing the page.
# It runs with no network, and two runs write the same bytes: the copy
# is the whole program's output.
import json
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

COMPETITION = "news-image-20261124"
DATE = "2026-11-24"
WEEKDAY = "Tuesday"
TITLE = "The Whole Wide Tuesday"
STORIES = 35
ILLUSTRATED = 11
REGIONS = 7
FIELDS = 20

HEROES = [
    "Russia says it downed 699 Ukrainian drones overnight; a Russian drone briefly enters Polish airspace",
    "Iraq's PM Ali al-Zaidi orders a federal takeover of oilfields in four Kurdish-held provinces",
    "Malaysia to return more than 6,500 Myanmar nationals in December, days after the ICJ genocide ruling",
]

REGIONS_COUNT = {
    "Europe": 9,
    "Middle East": 4,
    "Asia": 9,
    "Africa": 3,
    "Americas": 4,
    "Oceania": 4,
    "Global": 2,
}

NUMBERS = {
    "ukrainian_drones_downed_claimed": 699,
    "drones_bound_for_moscow_region": 355,
    "iraqi_provinces_taken_over": 4,
    "myanmar_nationals_to_return": 6500,
    "eu_china_hybrid_cap_per_year": 350000,
    "women_girls_killed_by_kin_2025": 47000,
    "venezuela_debt_usd_bn": 237.5,
    "hanoi_killed": 6,
    "hanoi_injured": 10,
    "gaza_meningitis_cases_october": 272,
    "donald_runs": 85,
    "donald_balls": 32,
}


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(OUT_DIR, "entry.png")
    shutil.copyfile(src, dst)
    dossier = {
        "competition": COMPETITION,
        "date": DATE,
        "weekday": WEEKDAY,
        "title": TITLE,
        "stories": STORIES,
        "illustrated": ILLUSTRATED,
        "regions": REGIONS_COUNT,
        "fields": FIELDS,
        "heroes": HEROES,
        "numbers": NUMBERS,
        "output": dst,
        "bytes": os.path.getsize(dst),
    }
    print(json.dumps(dossier, ensure_ascii=False))


if __name__ == "__main__":
    main()
