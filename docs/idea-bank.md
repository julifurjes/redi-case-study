# Workshop Idea Bank

Early options for the ReDI Python workshop. These are starting points, not settled story or dataset decisions. Every person, organization, and record should be fictional.

## What makes a good case

- One clear question students can answer with evidence from more than one file.
- A small core dataset that can be explored with ordinary Python, with Pandas as an optional shortcut.
- Realistic messiness: inconsistent names or times, missing fields, duplicates, and at least one misleading clue.
- A conclusion that is supported by the records, while leaving room to say what the data cannot prove.
- Optional hints and a stretch task that do not block the core investigation.

## Case concepts

### The missing maker-fair mascot

**Question:** Where did the handmade robot mascot go between the final workshop and the awards ceremony?

Students compare an equipment sign-out sheet, room and event schedule, volunteer notes, and a short incident log. They standardize room names and timestamps, spot a duplicate sign-out, then match the mascot's last confirmed location to the event timeline. The answer key can distinguish the last place it was recorded from the place it was ultimately found, so students need to explain the strength of their evidence.

**Why it could work:** A tangible, low-stakes mystery; easy to understand without specialist knowledge; naturally combines structured records with a few short text clues.

### The surprise at the community market

**Question:** Why did one popular stall run out early, and was the shortage predictable?

Students join order totals, delivery records, and a stall schedule. They clean product names and quantities, identify a late or miscounted delivery, and chart demand over time. The resolution should separate what the records show from guesses about why visitors preferred one item.

**Why it could work:** Gives a clear charting payoff and approachable business context. It may feel more like an operations exercise than a mystery, so the characters and story need extra care.

### The mixed-up film-night playlist

**Question:** Which version of the playlist was actually played, and why did the schedule drift?

Students compare a run sheet, volunteer handover notes, and timestamped playback records. They reconcile track titles and time formats, remove duplicate entries, and build a timeline. A late start or unrecorded change can explain the drift without requiring students to infer anyone's intent.

**Why it could work:** A lively event setting with a natural timeline. The files need a carefully designed answer key so several plausible explanations do not become equally likely.

## Recommended starting point: The missing maker-fair mascot

This seems the strongest first prototype: it has a simple central question, supports multiple Python skills, and makes it natural to distinguish a confirmed fact from an assumption. Keep the core investigation to three or four files:

| File | Example fields | Useful data wrinkle |
| --- | --- | --- |
| `equipment_log.csv` | item, person, room, checked_out, returned | Inconsistent item and room names; one duplicate row |
| `event_schedule.csv` | activity, room, start_time, end_time | A few times use different formats |
| `volunteer_notes.csv` | time, location, note | Missing time on one note; short clue text |
| `room_directory.csv` | room_code, display_name | Maps room codes to names used in other files |

The core answer should be recoverable by cleaning names and times and comparing the event timeline with the equipment log. Include enough evidence to identify the mascot's last confirmed location, but do not claim a precise final location unless a record supports it.

### Possible student path

1. Read each file and inspect row counts, columns, and a few example values.
2. Find missing values, duplicate records, and inconsistent room or item names.
3. Use a small function to normalize a room name or timestamp; use a dictionary to map room codes.
4. Compare the cleaned records to find the mascot's last confirmed location and the relevant activities.
5. Make a simple timeline or bar chart and write a short finding with one uncertainty.

### Hints and stretch ideas

- **Hint 1:** Start with the equipment log and filter for the mascot.
- **Hint 2:** Room labels that look different may refer to the same room; check the room directory.
- **Stretch:** Compare planned and actual event timing, or write a function that flags records with missing or inconsistent values.

### Answer-key guardrails

- Write the intended conclusion before generating the data, then generate records to support it consistently.
- Mark which records are confirmed evidence, which are clues, and which are intentionally unreliable.
- Avoid requiring students to guess a person's motive or treat a missing record as proof.
- Keep a clean source version of each dataset so the answer key can explain every introduced data issue.

## Decisions to make next

- Confirm whether the maker-fair story fits the audience and workshop length.
- Decide if students investigate only the last confirmed location or also receive a later recovery clue.
- Set a target dataset size that leaves room for manual Python exploration before introducing Pandas.
- Draft the answer key and test the mystery before producing the student-facing files.