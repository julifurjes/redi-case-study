"""Generate fictional festival-parade investigation data."""

import argparse
import csv
import random
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def write_csv(path, fieldnames, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def generate(output_dir, seed):
    rng = random.Random(seed)

    planned_route = [
        {"stop_order": 1, "planned_time": "13:55", "location": "North Gate"},
        {"stop_order": 2, "planned_time": "14:02", "location": "Fountain"},
        {"stop_order": 3, "planned_time": "14:17", "location": "Music Corner"},
        {"stop_order": 4, "planned_time": "14:27", "location": "Art Tent"},
        {"stop_order": 5, "planned_time": "14:41", "location": "Main Stage"},
    ]

    parade_log = [
        {
            "log_id": "P01",
            "timestamp": "13:55",
            "location": "North Gate",
            "event": "Parade assembled",
            "marshal_note": "Ready to go",
        },
        {
            "log_id": "P02",
            "timestamp": "14:02",
            "location": "Fountain",
            "event": "Scheduled pass",
            "marshal_note": "On the printed route",
        },
        {
            "log_id": "P03",
            "timestamp": "14:09",
            "location": "Paper Plane tent",
            "event": "Unexpected stop",
            "marshal_note": "A small paper sun appeared on the float",
        },
        {
            "log_id": "P04",
            "timestamp": "14:17",
            "location": "Music Corner",
            "event": "Scheduled pass",
            "marshal_note": "Band played the short version",
        },
        {
            "log_id": "P05",
            "timestamp": "2:24 PM",
            "location": "Repair Cafe",
            "event": "Unexpected stop",
            "marshal_note": "Someone tied a bright ribbon to the float",
        },
        {
            "log_id": "P06",
            "timestamp": "14:33",
            "location": "Oak Corner",
            "event": "Unexpected stop",
            "marshal_note": "Crowd sang the festival jingle",
        },
        {
            "log_id": "P07",
            "timestamp": "14:48",
            "location": "Main Stage",
            "event": "Finale",
            "marshal_note": "Parade arrived seven minutes late",
        },
        {
            "log_id": "P08",
            "timestamp": "14:12",
            "location": "Tea Stall",
            "event": "Passed by",
            "marshal_note": "Crowd waved; parade did not stop",
        },
    ]
    parade_log.append(next(row for row in parade_log if row["log_id"] == "P05").copy())

    volunteer_help = [
        {
            "help_id": "H01",
            "timestamp": "14:05",
            "location": "Kids' Plane Table",
            "helper_name": "Mira Chen",
            "problem": "Wind flipped the paper-plane target",
            "fix": "Taped the target back onto its stand",
        },
        {
            "help_id": "H02",
            "timestamp": "14:19",
            "location": "Tool Tent",
            "helper_name": "Mira Chen",
            "problem": "The welcome banner came loose",
            "fix": "Found a spare clip and put it back up",
        },
        {
            "help_id": "H03",
            "timestamp": "14:28",
            "location": "Oak Shade",
            "helper_name": "Mira Chen",
            "problem": "The site map fell over",
            "fix": "Propped it up with a box of donated books",
        },
        {
            "help_id": "H04",
            "timestamp": "14:10",
            "location": "Tea Stall",
            "helper_name": "Lee Park",
            "problem": "A stack of cups wobbled",
            "fix": "Moved the cups to a level table",
        },
        {
            "help_id": "H05",
            "timestamp": "14:30",
            "location": "Art Tent",
            "helper_name": "",
            "problem": "The sign was hard to see from the path",
            "fix": "Turned the sign toward the walkway",
        },
        {
            "help_id": "H06",
            "timestamp": "13:48",
            "location": "Music Corner",
            "helper_name": "Mira Chen",
            "problem": "A music stand was missing a clip",
            "fix": "Borrowed one from the information desk",
        },
    ]

    location_aliases = [
        {"raw_location": "North Gate", "canonical_location": "North Gate"},
        {"raw_location": "Fountain", "canonical_location": "Fountain"},
        {"raw_location": "Music Corner", "canonical_location": "Music Corner"},
        {"raw_location": "Art Tent", "canonical_location": "Art Tent"},
        {"raw_location": "Main Stage", "canonical_location": "Main Stage"},
        {"raw_location": "Paper Plane tent", "canonical_location": "Paper Plane Tent"},
        {"raw_location": "Kids' Plane Table", "canonical_location": "Paper Plane Tent"},
        {"raw_location": "Repair Cafe", "canonical_location": "Repair Cafe"},
        {"raw_location": "Tool Tent", "canonical_location": "Repair Cafe"},
        {"raw_location": "Oak Corner", "canonical_location": "Oak Corner"},
        {"raw_location": "Oak Shade", "canonical_location": "Oak Corner"},
        {"raw_location": "Tea Stall", "canonical_location": "Tea Stall"},
    ]

    finale_note = [
        {
            "note_id": "N01",
            "found_at": "Main Stage",
            "message": (
                "For the parade team: make three little detours to the places "
                "where someone made today easier. Meet us at the finale with "
                "the paper sun. Please keep the surprise quiet."
            ),
        }
    ]

    rng.shuffle(parade_log)
    rng.shuffle(volunteer_help)
    rng.shuffle(location_aliases)

    write_csv(
        output_dir / "planned_route.csv",
        ["stop_order", "planned_time", "location"],
        planned_route,
    )
    write_csv(
        output_dir / "parade_log.csv",
        ["log_id", "timestamp", "location", "event", "marshal_note"],
        parade_log,
    )
    write_csv(
        output_dir / "volunteer_help.csv",
        ["help_id", "timestamp", "location", "helper_name", "problem", "fix"],
        volunteer_help,
    )
    write_csv(
        output_dir / "location_aliases.csv",
        ["raw_location", "canonical_location"],
        location_aliases,
    )
    write_csv(
        output_dir / "new_evidence" / "finale_note.csv",
        ["note_id", "found_at", "message"],
        finale_note,
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT / "data",
        help="directory for generated CSV files (default: %(default)s)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="seed controlling the order of unsorted records (default: %(default)s)",
    )
    args = parser.parse_args()
    generate(args.output_dir, args.seed)
    print(f"Generated festival CSV files in {args.output_dir}")


if __name__ == "__main__":
    main()