"""Starter for the festival-parade data investigation."""

import csv
from pathlib import Path


DATA_DIR = Path(__file__).resolve().parents[1] / "data"


def read_csv(filename):
    """Read a CSV file from the project's data folder."""
    path = DATA_DIR / filename
    with path.open("r", newline="", encoding="utf-8") as csv_file:
        return list(csv.DictReader(csv_file))


def show_preview(title, rows, limit=5):
    """Print a small sample of rows so the data is easy to inspect."""
    print(f"\n{title} ({len(rows)} rows)")
    for row in rows[:limit]:
        print(row)


planned_route = read_csv("planned_route.csv")
parade_log = read_csv("parade_log.csv")
volunteer_help = read_csv("volunteer_help.csv")
location_aliases = read_csv("location_aliases.csv")

show_preview("Planned route", planned_route)
show_preview("Parade log", parade_log)
show_preview("Volunteer help", volunteer_help)
show_preview("Location aliases", location_aliases)

# Investigation tasks:
# 1. Count the different event types in parade_log.
# 2. Check for duplicate log entries before building a timeline.
# 3. Use location_aliases to compare locations across the files.
# 4. Put the events in time order, even when timestamps use different formats.
# 5. Compare the unexpected stops with volunteer_help and write a finding.