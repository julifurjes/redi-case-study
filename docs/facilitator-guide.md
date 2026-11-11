# Facilitator guide - spoilers

Do not distribute this file, the reference solver, or tests to students.
The repository is not spoiler-free; distribute the allowlisted student ZIP.

## Teaching goals and timing

Designed for the final third of an introductory Python course: students
should know functions, lists, dictionaries, loops, and conditionals. CSV and
Decimal usage can be introduced with the supplied notebook. No accounting,
Pandas, joins, HTTP, or database knowledge is required.

Allow **45 minutes** for the full brief, or **30 minutes** with loading
pre-run, no chart, and a short oral verdict. Reserve another 5-10 minutes
for debrief if possible. Have pairs swap driver/checker roles halfway.
These are suggested timings, not classroom-tested estimates.

| Phase | Full session | Watch for |
| --- | --- | --- |
| Brief and inspect | 5 min | Treating a CSV as comma-split text |
| Clean | 10 min | Deduplicating by person, dropping blank messages |
| Calculate | 10 min | Case-sensitive status checks, counting pending cash |
| Cross-check evidence | 10 min | Subtracting receipts twice, confusing reimbursement and refund |
| Report | 10 min | An accusation unsupported by the records |

All three files are available from the start. Optionally ask students to
calculate first and open chat later, but do not withhold account rules.
The chat explains timing; it never states the cash balance or shortfall.
Students must reconcile the export to establish the numerical verdict.

## Prepare and distribute

From the repository root:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/solve_case.py
python3 scripts/build_student_pack.py
```

Share only `dist/festival-student-pack.zip`. It contains a student README,
brief, hints, three CSVs, an output-free scaffold notebook, and optional
notebook dependencies. The builder refuses to replace an existing ZIP;
use `--output` with a new filename when building another version.
No server or network access is required for the core investigation.
Preinstall the notebook dependencies if students will be offline.

## Exact answer key

The fund opens at **0 DKK**. At 11 June 2026, 12:00:

| Item | DKK | Evidence |
| --- | ---: | --- |
| 30 tickets at 150 | 4,500 | PAY-001 through PAY-030, after removing exact duplicates |
| Sponsorship | 500 | PAY-031 / SPONSOR-01 |
| Completed income | **5,000** | Unique completed incoming payments |
| Flamingos | 870 | PAY-032 / REC-001 / FLAMINGOS-01 |
| Speaker deposit reimbursement | 600 | PAY-033 / REC-002 / SPEAKER-01 |
| Snacks | 900 | PAY-034 / REC-003 / SNACKS-01 |
| Posters | 300 | PAY-035 / REC-004 / POSTERS-01 |
| Supplies | 200 | PAY-036 / REC-005 / SUPPLIES-01 |
| Completed spending | **2,870** | Five completed outgoing payments |
| Cash available | **2,130** | 5,000 - 2,870 |
| Unpaid DJ invoice | **2,500** | REC-006 / DJ-01, due 12 June |
| Shortfall | **370** | 2,500 - 2,130 |
| Approved but pending flamingo refund | **870** | PAY-037; chat expects settlement 16 June |
| Conditional balance after refund | **3,000** | 2,130 + 870, not current cash |
| Conditional remainder after paying DJ | **500** | 2,130 + 870 - 2,500 |

The DJ cannot be paid in full from current funds. A refund arriving on its
expected date cannot meet the DJ's deadline. A practical response is to
seek a documented temporary contribution or negotiate payment timing, not
silently assume a pending payment is available.

Oliver's "got the speaker deposit money back" means the **fund reimbursed
his personal outlay**, not that Sound Sprout returned its security deposit.
The company still holds 600 DKK until equipment is returned undamaged on
13 June. That is after the festival, and settlement is not guaranteed by
these records. It is not a second completed incoming payment. REC-002 is
the purchase evidence behind the reimbursement, not another fund expense.

Supported conclusion: a **cash-timing problem and misunderstood records**.
There is **no evidence establishing theft**. Do not equate that statement
with proving nobody could have acted improperly outside these records.

## Intentional data issues

- 39 payment rows, 37 unique IDs, 36 completed transactions, 1 pending.
- PAY-003 and PAY-019 are each exported twice, with exactly identical rows.
  Removing the two extras prevents overstating income by 300 DKK.
- PAY-008 and PAY-030 are two legitimate Oliver ticket purchases; the
  second is for Robin. Different IDs and references must remain.
- Spaces occur around Alma, Ella, Anna, and the reimbursement recipient.
- Status case varies; amounts use comma or point decimal notation.
- PAY-028 has an empty optional message and must remain in the totals.
- FLAMINGOS-01 connects a completed expense and pending refund; reference
  is not a transaction key. Match direction and status as well.

## Hints and debrief

Release hints progressively rather than displaying all methods immediately.
Accept standard-library or Pandas solutions and equivalent labelled tables.
For a merge stretch, filter to the five completed expenses first; they can
join one-to-one to receipts. Joining all payments leaves ticket/sponsor
references unmatched and duplicates the flamingo receipt across two rows.

Common diagnostic totals:

- **2,430 DKK:** the duplicate tickets were counted.
- **3,000 DKK available now:** the pending refund was counted as settled.
- **2,730 DKK:** the held speaker deposit was incorrectly added to current cash.
- A negative result can arise from subtracting purchase receipts a second time.

Ask teams to identify the exact row or message that changed their initial
hypothesis, and one fact they would need to verify with the committee.
An optional chart should show the five completed expense categories, with
DKK labels; don't require visualization in a compressed 30-minute session.

## Assessment (10 points)

- **3:** defensible cleaning, including exact duplicates vs repeat purchasers.
- **3:** reproducible income, spending, balance, and DJ shortfall.
- **2:** receipt/reference reasoning and separation of pending/current cash.
- **2:** clear evidence-based verdict, timing, uncertainty, and next step.

Do not award full reconciliation credit for correct numbers without code.
Do not penalize a sound standard-library solution for not using Pandas.

## Maintaining the case

The checked-in CSVs are the source of truth; no generator is needed for this
small fixture. Change evidence and its answer key together, then rerun the
tests and solver. Tests protect exact totals, deliberate messiness,
reference matching, notebook startup, and the spoiler-free ZIP allowlist.
