# Graduated hints

Try one hint at a time; these give methods rather than the final totals.

## 1. Loading

Use `csv.DictReader` with `encoding="utf-8"` and `newline=""`. Each row is a
dictionary whose values are strings. Print `rows[0]` and `len(rows)`.

## 2. Cleaning text and money

`text.strip()` removes surrounding spaces and `text.strip().lower()` makes
status comparisons consistent. For these files, `Decimal(text.replace(",", "."))`
handles both decimal separators exactly. Import `Decimal` from `decimal`.
Do not delete a transaction because its optional message is empty.

## 3. Duplicate identity

Group or index by `payment_id`, not sender, amount, or reference. Compare the
full original rows when an ID repeats. Remove a row only when it is an exact
export duplicate; stop and investigate conflicting records. Check the two
different ticket references associated with Oliver.

## 4. Cash direction

Start at zero. For each unique, completed payment, add the amount if the
recipient is the fund and subtract it if the sender is the fund. Keep pending
amounts in a separate list. Print subtotals before calculating the balance.

## 5. Receipts and timing

Find `DJ-01` in receipts. Is there a completed payment with that reference?
Match the five outgoing purchase references manually before trying a merge.
Never subtract the receipts again after subtracting their payments.

## 6. The misleading message

Follow `SPEAKER-01`: who first paid the rental company, and who later paid
Oliver? Which account still holds the deposit? Then check the refund's
status and expected date against the DJ's deadline.

## 7. A conditional calculation is not today's balance

Try `current_balance + pending_refund - dj_invoice` for the refund scenario.
Label it conditional and explain whether the refund is expected before the
festival. Do not treat approval as settlement or uncertainty as misconduct.
