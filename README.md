# ReDI Python Workshop

A playful investigation workshop for students in the final third of an introductory Python course.

**Case: The festival fund fiasco.** Students must establish how much money is
actually available, whether the DJ can be paid, and what explains the shortfall.
The materials are ready for a facilitator dry run; classroom timing has not
yet been validated.

Students will use Python to explore evidence, clean messy data, and explain what they find. The aim is a fun mystery with a clear payoff and room for different approaches.

## Learning goals

- Read and explore data from files.
- Use functions, lists, dictionaries, conditionals, and loops.
- Identify missing values, inconsistent formats, and duplicate records.
- Combine clues across datasets using Pandas where useful.
- Communicate findings with a short explanation and an optional chart.
- Distinguish evidence from assumptions and unresolved questions.

## Repository structure

| Location | Contents |
| --- | --- |
| [data/](data/) | Three fictional CSVs: payments, receipts, chat |
| [Student brief](docs/student-brief.md) | Account rules, tasks, and submission criteria |
| [Scaffold notebook](notebooks/festival-investigation.ipynb) | Loading code, investigation prompts, and student TODOs |
| [Hints](docs/hints.md) | Progressive help without final totals |
| [Student setup](STUDENT_README.md) | Notebook and no-install Python routes |
| [Facilitator guide](docs/facilitator-guide.md) | **Spoilers:** answer key, timing, rubric, misconceptions |
| [scripts/](scripts/) | Reference reconciliation and student ZIP builder |
| [tests/](tests/) | Dataset, arithmetic, notebook, and distribution checks |

The [idea bank](docs/idea-bank.md) is historical background, not the current
workshop specification.

## Workshop design

- Give students a mystery to solve and characters to care about.
- Make the core task achievable, with optional hints and stretch challenges.
- Use entirely fictional data suitable for sharing with external students.
- Keep the company connection to familiar, publicly known concepts.
- Introduce new evidence partway through if it makes the investigation more fun.

## Getting started

Use **Python 3.10+**. The core case and all facilitator checks use only the
standard library. Run from the repository root:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/solve_case.py
python3 scripts/build_student_pack.py
```

**Facilitators:** the solver prints spoilers. Share only the generated
`dist/festival-student-pack.zip`, not this repository: solutions and tests
deliberately remain outside the student pack. The builder refuses to
overwrite an existing archive; supply `--output path/to/new-pack.zip` to
create another version.

**Students:** follow [the setup guide](STUDENT_README.md) for a no-install
script route or Jupyter/VS Code notebook setup. Optional notebook and
stretch dependencies are in [requirements.txt](requirements.txt).

## Workshop scope

- Three small CSV files with a controlled set of cleaning issues.
- Approximately 45 minutes, or 30 minutes with loading prepared and no chart.
- Standard-library core, optional Pandas merge and charting stretches.
- Current cash, future refunds, and evidence versus assumptions kept distinct.
- No local server needed; after setup the investigation works offline.

Before classroom use, dry-run the notebook in the students' environment and
adjust timing for their experience.
