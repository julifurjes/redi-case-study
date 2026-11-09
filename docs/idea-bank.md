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

## Current prototype: The parade that wouldn't stay on route

At a warm, slightly chaotic pop-up festival, the parade makes three unexpected stops and arrives late. Students are data detectives asked to work out whether the detours were random or deliberate. The working reveal is that each detour visits a place where Mira Chen, a quiet fixer, solved a problem shortly beforehand. A note released later hints that the stops were planned as a thank-you.

The generator is `scripts/generate_data.py`. It uses only Python's standard library and writes these files:

| File | Purpose | Data wrinkle |
| --- | --- | --- |
| `data/planned_route.csv` | The published parade schedule | Baseline for comparison |
| `data/parade_log.csv` | What marshals recorded on the day | Unsorted rows, a duplicate entry, mixed time formats, and alternate place names |
| `data/volunteer_help.csv` | Problems volunteers solved around the festival | Alternate place names and one missing helper name |
| `data/location_aliases.csv` | Maps recorded place names to shared names | Students can use a dictionary or join to reconcile locations |
| `data/new_evidence/finale_note.csv` | A clue about the reason for the detours | Hold back until students have formed an initial theory |

### Possible student path

1. Compare the planned route with the parade log and identify the three unexpected stops.
2. Remove the duplicate log entry and put mixed-format times in order.
3. Use the location aliases to compare parade stops with the volunteer-help records.
4. Notice that Mira helped at each detour location shortly before the parade arrived.
5. Read the finale note and explain the likely thank-you, separating evidence from assumption.

### Hints and stretch ideas

- **Hint 1:** Find rows in the parade log where the event is `Unexpected stop`.
- **Hint 2:** The same place can appear under different names in different files; check `location_aliases.csv`.
- **Stretch:** Make a timeline of help and parade events, or write a function that standardizes the different timestamp formats.

### Answer-key guardrails

- The three unexpected stops are the Paper Plane Tent, Repair Cafe, and Oak Corner; each has a nearby help record for Mira.
- The finale note supports the thank-you interpretation, but students should cite the records rather than infer anyone's motive from a missing value.
- Keep `finale_note.csv` separate from the first evidence bundle so the reveal can be timed during the workshop.

## Decisions to make next

- Confirm the parade story and whether the thank-you reveal works for the audience.
- Confirm workshop length and student prerequisites.
- Finalize the core task, hints, and stretch challenges.
- Validate the generated records against a facilitator answer key.
- Try the workshop from a student perspective.