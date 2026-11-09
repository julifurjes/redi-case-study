# The Parade That Wouldn't Stay on Route

## The case

The neighborhood festival parade did not follow its printed route exactly. Marshals recorded several unexpected stops, and the parade arrived late at the main stage. The organizers have collected a few files, but the records are messy and do not tell the whole story on their own.

You are a festival data detective. Reconstruct what was planned, compare it with what happened, and report what the evidence does and does not support.

## Your files

- `data/planned_route.csv` lists the published parade stops and times.
- `data/parade_log.csv` contains the marshals' notes from the day.
- `data/volunteer_help.csv` records some problems volunteers handled around the festival.
- `data/location_aliases.csv` maps different recorded place names to shared names.

## Investigation

1. **Get oriented.** Run `notebooks/investigation_starter.py`. For each file, record its row count and columns. Count the event types in the parade log and note any blank values.
2. **Rebuild the timeline.** Compare the planned route with the parade log. Find the unexpected stops, check whether any log entries repeat, and put the events in time order. Some timestamps use different formats.
3. **Connect the records.** Use `location_aliases.csv` to reconcile place names, then compare the parade stops with the volunteer-help records. Record the IDs, locations, times, and names that support a match.
4. **Form a theory.** Write down what you observed, what you think it means, and what remains uncertain. Your first explanation can change if your instructor shares more evidence later.

You can use basic Python, and Pandas if your instructor has introduced it. You do not need to use every column or clean every issue to make a useful finding.

### Hints

- Start by filtering for rows where the parade-log event is `Unexpected stop`.
- Compare both the log ID and the other fields before deciding whether two rows are duplicates.
- Build a dictionary from `location_aliases.csv` so different names can be compared consistently.

### Stretch

Make a timeline that shows both volunteer-help records and parade events. If Pandas is available, chart the planned and actual Main Stage arrival times.

## Share your finding

Prepare a short explanation and one simple chart or timeline. Include:

- What changed between the planned route and the recorded parade.
- At least two supporting records from different files.
- One uncertainty or question the available data cannot answer.

Before removing a duplicate, check whether it is an exact repeat. A blank value means the information was not recorded; it does not prove that something did not happen.
