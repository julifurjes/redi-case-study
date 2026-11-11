"""Facilitator-only reference reconciliation. Uses the Python standard library."""

import argparse
import csv
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUND = "Festival Fund"
CUTOFF = datetime(2026, 6, 11, 12)


@dataclass(frozen=True)
class Payment:
    payment_id: str
    timestamp: datetime
    sender: str
    recipient: str
    amount: Decimal
    status: str
    reference: str
    message: str


@dataclass(frozen=True)
class Report:
    raw_count: int
    payments: tuple[Payment, ...]
    income: Decimal
    spending: Decimal
    balance: Decimal
    dj_invoice: Decimal
    shortfall: Decimal
    pending_refund: Decimal
    after_refund_and_dj: Decimal
    spending_by_reference: dict[str, Decimal]


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or len(set(reader.fieldnames)) != len(reader.fieldnames):
            raise ValueError(f"{path.name}: missing or duplicate column names")
        rows = []
        for line, row in enumerate(reader, start=2):
            if None in row or any(value is None for value in row.values()):
                raise ValueError(f"{path.name}:{line}: wrong number of CSV fields")
            rows.append(row)
        return rows


def parse_money(text: str) -> Decimal:
    amount = Decimal(text.strip().replace(",", "."))
    if not amount.is_finite() or amount <= 0 or amount != amount.quantize(Decimal("0.01")):
        raise ValueError(f"Expected a positive DKK amount with at most two decimals: {text!r}")
    return amount


def clean_payments(rows: list[dict[str, str]]) -> list[Payment]:
    originals: dict[str, dict[str, str]] = {}
    cleaned = []
    for row in rows:
        payment_id = row["payment_id"].strip()
        if not payment_id:
            raise ValueError("Payment ID cannot be blank")
        if payment_id in originals:
            if row != originals[payment_id]:
                raise ValueError(f"Conflicting duplicate payment ID: {payment_id}")
            continue
        originals[payment_id] = row
        status = row["status"].strip().lower()
        if status not in {"completed", "pending"}:
            raise ValueError(f"{payment_id}: unknown status {status!r}")
        sender, recipient = row["sender"].strip(), row["recipient"].strip()
        reference = row["reference"].strip()
        if not sender or not recipient or not reference:
            raise ValueError(f"{payment_id}: sender, recipient and reference are required")
        if (sender == FUND) == (recipient == FUND):
            raise ValueError(f"{payment_id}: exactly one account must be {FUND}")
        timestamp = datetime.fromisoformat(row["timestamp"])
        if timestamp > CUTOFF:
            raise ValueError(f"{payment_id}: transaction is after the investigation cutoff")
        cleaned.append(Payment(
            payment_id, timestamp, sender, recipient, parse_money(row["amount_dkk"]),
            status, reference, row["message"].strip(),
        ))
    return cleaned


def reconcile(data_dir: Path) -> Report:
    raw = load_csv(data_dir / "payments.csv")
    payments = clean_payments(raw)
    receipts = load_csv(data_dir / "receipts.csv")
    receipts_by_reference: dict[str, dict[str, str]] = {}
    for receipt in receipts:
        reference = receipt["reference"].strip()
        if not reference or reference in receipts_by_reference:
            raise ValueError(f"Missing or repeated receipt reference: {reference!r}")
        if receipt["status"].strip().lower() not in {"paid", "unpaid"}:
            raise ValueError(f"{reference}: unknown receipt status")
        parse_money(receipt["amount_dkk"])
        receipts_by_reference[reference] = receipt

    completed = [payment for payment in payments if payment.status == "completed"]
    income = sum((p.amount for p in completed if p.recipient == FUND), Decimal("0.00"))
    outgoing = [p for p in completed if p.sender == FUND]
    spending = sum((p.amount for p in outgoing), Decimal("0.00"))
    spending_by_reference: dict[str, Decimal] = {}
    for payment in outgoing:
        receipt = receipts_by_reference[payment.reference]
        if receipt["status"].strip().lower() != "paid":
            raise ValueError(f"{payment.reference}: completed payment has an unpaid receipt")
        spending_by_reference[payment.reference] = (
            spending_by_reference.get(payment.reference, Decimal("0.00")) + payment.amount
        )
    for reference, amount in spending_by_reference.items():
        if amount != parse_money(receipts_by_reference[reference]["amount_dkk"]):
            raise ValueError(f"{reference}: completed expense does not match receipt amount")

    dj = receipts_by_reference["DJ-01"]
    if dj["status"].strip().lower() != "unpaid":
        raise ValueError("This case expects an unpaid DJ invoice")
    if any(p.reference == "DJ-01" for p in completed):
        raise ValueError("DJ invoice is marked unpaid but has a completed payment")
    dj_invoice = parse_money(dj["amount_dkk"])
    pending_refund = sum((
        p.amount for p in payments
        if p.status == "pending" and p.recipient == FUND and p.reference == "FLAMINGOS-01"
    ), Decimal("0.00"))
    balance = income - spending
    return Report(
        len(raw), tuple(payments), income, spending, balance, dj_invoice,
        max(dj_invoice - balance, Decimal("0.00")), pending_refund,
        balance + pending_refund - dj_invoice, spending_by_reference,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=ROOT / "data")
    args = parser.parse_args()
    report = reconcile(args.data_dir)
    print("FACILITATOR SOLUTION - do not distribute to students")
    print(f"Payment rows: {report.raw_count} raw -> {len(report.payments)} unique")
    for label, amount in (
        ("Completed income", report.income),
        ("Completed spending", report.spending),
        ("Available now", report.balance),
        ("Unpaid DJ invoice", report.dj_invoice),
        ("Shortfall now", report.shortfall),
        ("Pending flamingo refund (not cash)", report.pending_refund),
        ("IF refund settles, remainder after DJ", report.after_refund_and_dj),
    ):
        print(f"{label}: {amount:.2f} DKK")
    print("Completed spending by reference:")
    for reference, amount in report.spending_by_reference.items():
        print(f"  {reference}: {amount:.2f} DKK")
    print("The refund is expected on 16 June, after the 12 June DJ deadline.")
    print("Oliver was reimbursed; Sound Sprout still holds the speaker deposit.")
    print("Supported conclusion: cash timing and misunderstood records; theft is not established.")


if __name__ == "__main__":
    main()
