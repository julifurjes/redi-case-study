# Facilitator Guide: The Parade That Wouldn't Stay on Route

**Facilitator copy. Do not distribute with the student brief.** This is a draft answer key for the current generated data.

## Intended conclusion

The strongest explanation is that the three unexpected parade stops were deliberate parts of a quiet surprise for Mira Chen. At each stop, the volunteer-help log shows Mira solving a problem at the same place shortly before the parade arrived. The later note says to make three detours to places where someone made the festival day easier and to bring the paper sun to the finale.

This is a well-supported interpretation, not a complete proof: the note does not name Mira or say who wrote it. Students should describe the connection as likely and cite the records.

## Evidence trail

| Parade record | Recorded stop | Matching help record | Time gap |
| --- | --- | --- | --- |
| P03, 14:09 | Paper Plane tent | H01, Kids' Plane Table, Mira Chen, 14:05 | 4 minutes |
| P05, 14:24 | Repair Cafe | H02, Tool Tent, Mira Chen, 14:19 | 5 minutes |
| P06, 14:33 | Oak Corner | H03, Oak Shade, Mira Chen, 14:28 | 5 minutes |

The location-alias file connects each pair of different place names. P03 also records a paper sun appearing on the float; the finale note asks the parade team to bring the paper sun to the finale.

## Data issues and discussion points

- `parade_log.csv` is shuffled. Sort by time before describing the sequence.
- P05 appears twice with the same ID and values. Count it once; it is a duplicate record, not a second stop.
- Most times use a 24-hour format, while P05 uses `2:24 PM`, which is 14:24.
- Parade and help logs use different names for the three detour locations. Use `location_aliases.csv` to reconcile them.
- H05 has a blank helper name. The data does not identify who handled that sign, so leave the name unknown.
- Mira also helped at Music Corner, a scheduled parade stop. Not every help record corresponds to an unexpected stop.
- Lee helped at Tea Stall shortly before the parade passed by, but the marshal log says the parade did not stop there. Timing alone does not establish a connection.
- The plan lists Art Tent at 14:27, but the parade log has no corresponding Art Tent event. Do not claim the parade skipped it based only on the missing log entry.

## Timing check

The planned Main Stage arrival is 14:41. The parade log records the finale at 14:48, seven minutes later.

## Suggested release order

1. Give students `planned_route.csv`, `parade_log.csv`, `volunteer_help.csv`, and `location_aliases.csv` first.
2. Let them identify and compare the unexpected stops before sharing the additional clue.
3. Then release `new_evidence/finale_note.csv` and ask whether it changes their explanation.
4. In the debrief, distinguish the recorded facts, the likely thank-you explanation, and the remaining uncertainties.
