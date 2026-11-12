# The festival fund fiasco

The festival is tomorrow, the stage is full of inflatable flamingos, and DJ
Comet wants paying. The committee's chat is confused. You are the evidence team.

**Your questions:** How much money is actually available? Can the DJ be paid
in full on time? What explains any shortfall?

All people, organizations, messages, and transactions are fictional.

## Rules of this fictional account

- Investigate as of **11 June 2026 at 12:00**, before the festival on 12 June.
  The export covers all activity since the fund opened with **0 DKK**.
- Every amount is a positive magnitude in DKK. A completed payment **to**
  `Festival Fund` adds cash; a completed payment **from** it removes cash.
  Pending payments have not changed the balance.
- Payment IDs identify transactions. Repeated export rows are not extra money.
  A sender can legitimately buy more than one ticket.
- Receipts describe purchases or invoices, **not additional cash movements**.
  A paid receipt may have been paid personally and then reimbursed.
- Receipt `expected_date` means purchase date for a paid receipt and payment
  deadline for an unpaid invoice. It is not a promised refund date.
- Shared references connect evidence. A purchase and its refund can share a
  reference but have different payment IDs. Read the direction and status.
- No overdraft, credit, or other money is available in this case.

## Evidence

| File | What it contains |
| --- | --- |
| `data/payments.csv` | Payment export: ID, timestamp, sender, recipient, amount, status, reference, optional message |
| `data/receipts.csv` | Purchase receipts and an unpaid invoice: ID, reference, buyer, vendor, amount, status, description, expected date |
| `data/chat.csv` | Committee messages: timestamp, sender, message |

Timestamps are local festival time. Text may contain surrounding spaces;
statuses and decimal separators are inconsistent. An empty optional message
is valid. CSV quotes protect amounts containing commas: use a CSV reader,
not `line.split(",")`.

## Investigation

Work at your own pace and have fun exploring. If you work in pairs, take turns
driving and checking the evidence. There is nothing to hand in.

1. **Inspect.** Load all three files. Print their columns, row counts,
   and a few examples. Keep originals unchanged.
2. **Clean.** Normalize names, statuses, and amounts. Investigate
   repeated IDs before removing exact duplicate records. Record each decision.
3. **Reconcile.** Calculate completed incoming and outgoing totals
   separately, then the balance. Find the unpaid DJ invoice and calculate how
   much would remain, or how much more is needed.
4. **Explain.** Match outgoing references to receipts and read the
   chat. Explain the flamingo refund and the two different speaker-deposit
   movements. Separate current cash from a future scenario.
5. **Reflect.** What do you think happened, and what evidence supports it?
   Try a small chart if you feel like it.

Use the scaffold notebook or an ordinary Python script. Lists, dictionaries,
functions, loops, and conditionals are sufficient; Pandas is optional.
Open `docs/hints.md` only when stuck.

## Questions to explore

- Raw and cleaned payment row counts, cleaning decisions, and why two payments
  from the same person are not automatically duplicates.
- Completed income, completed spending, current balance, DJ invoice, and
  surplus or shortfall, with units and reproducible code.
- A reference-based explanation of spending, refund status and timing, and
  Oliver's reimbursement versus the rental company's deposit.
- A clearly labelled **if the approved refund settles** calculation.
- What is established, what is uncertain, and what could happen next?
  Do the records establish theft?

You are done when you feel ready and can explain your findings.

## Optional stretches

- Chart completed spending by reference; label axes and units.
- Use a Pandas merge to match expenses to receipts. Think about why joining
  *all* payments by reference can produce several rows per receipt.
- Add assertions to protect your totals or reject conflicting duplicate IDs.
- Calculate a second, explicitly conditional scenario for the rental deposit.
  Do not assume it will return on time or undamaged.
