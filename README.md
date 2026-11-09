# ReDI Python Workshop

A playful investigation workshop for students in the final third of an introductory Python course.

**Status: early prototype.** A fictional festival-parade story and CSV generator are in place; the workshop length, exercises, and final answer key are still to be decided.

Students will use Python to explore evidence, clean messy data, and explain what they find. The aim is a fun mystery with a clear payoff and room for different approaches.

## Learning goals

- Read and explore data from files.
- Use functions, lists, dictionaries, conditionals, and loops.
- Identify missing values, inconsistent formats, and duplicate records.
- Combine clues across datasets using Pandas where useful.
- Communicate findings with a chart and a short explanation.
- Distinguish evidence from assumptions and unresolved questions.

## Repository structure

```text
data/        Fictional datasets and supporting evidence
notebooks/   Student exercises and exploratory notebooks
scripts/     Dataset generation and supporting Python scripts
docs/        Case brief, workshop plan, and teaching notes
```

The parade CSVs are an initial data prototype. The [student case brief](docs/student-brief.md) and [Python investigation starter](notebooks/investigation_starter.py) are ready; guided exercises are still in development. Early story and dataset notes are in the [workshop idea bank](docs/idea-bank.md).

## Workshop design

- Give students a mystery to solve and characters to care about.
- Make the core task achievable, with optional hints and stretch challenges.
- Use entirely fictional data suitable for sharing with external students.
- Keep the company connection to familiar, publicly known concepts.
- Introduce new evidence partway through if it makes the investigation more fun.

## Getting started

The generator uses only Python's standard library. From the repository root, run:

```bash
python3 scripts/generate_data.py
```

This writes the core CSVs to `data/` and the staged finale clue to `data/new_evidence/`. Use `--seed` to change the order of unsorted records or `--output-dir` to choose another destination.

Run the dataset consistency checks with:

```bash
python3 -m unittest discover -s tests -v
```

## Next decisions

- [ ] Confirm the parade mystery and finalize its resolution.
- [ ] Confirm workshop length and student prerequisites.
- [ ] Define the core task, hints, and stretch challenges.
- [ ] Review the generated fictional datasets against a consistent answer key.
- [ ] Add student instructions and starter code.
- [ ] Decide how facilitator solutions will be kept separate from student materials.
- [ ] Try the workshop from a student perspective.
