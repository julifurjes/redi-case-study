"""Facilitator-only regression checks for the workshop evidence and student pack."""

from collections import Counter
from datetime import datetime
from decimal import Decimal, InvalidOperation
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest
from zipfile import ZipFile

from scripts.build_student_pack import build_pack
from scripts.solve_case import CUTOFF, FUND, clean_payments, load_csv, parse_money, reconcile


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


class EvidenceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.raw = load_csv(DATA / "payments.csv")
        self.report = reconcile(DATA)

    def test_exact_csv_schemas(self) -> None:
        expected = {
            "payments.csv": [
                "payment_id", "timestamp", "sender", "recipient",
                "amount_dkk", "status", "reference", "message",
            ],
            "receipts.csv": [
                "receipt_id", "reference", "buyer", "vendor",
                "amount_dkk", "status", "description", "expected_date",
            ],
            "chat.csv": ["timestamp", "sender", "message"],
        }
        for filename, columns in expected.items():
            with self.subTest(filename=filename):
                rows = load_csv(DATA / filename)
                self.assertTrue(rows)
                self.assertTrue(all(list(row) == columns for row in rows))

    def test_exact_totals_and_conditional_scenario(self) -> None:
        report = self.report
        self.assertEqual(report.raw_count, 39)
        self.assertEqual(len(report.payments), 37)
        self.assertEqual(Counter(p.status for p in report.payments), {"completed": 36, "pending": 1})
        self.assertEqual(report.income, Decimal("5000.00"))
        self.assertEqual(report.spending, Decimal("2870.00"))
        self.assertEqual(report.balance, Decimal("2130.00"))
        self.assertEqual(report.dj_invoice, Decimal("2500.00"))
        self.assertEqual(report.shortfall, Decimal("370.00"))
        self.assertEqual(report.pending_refund, Decimal("870.00"))
        self.assertEqual(report.after_refund_and_dj, Decimal("500.00"))
        self.assertEqual(report.spending_by_reference, {
            "FLAMINGOS-01": Decimal("870"),
            "SPEAKER-01": Decimal("600"),
            "SNACKS-01": Decimal("900"),
            "POSTERS-01": Decimal("300"),
            "SUPPLIES-01": Decimal("200"),
        })

    def test_only_two_exact_duplicate_ticket_rows(self) -> None:
        counts = Counter(row["payment_id"] for row in self.raw)
        self.assertEqual({key: count for key, count in counts.items() if count > 1},
                         {"PAY-003": 2, "PAY-019": 2})
        for payment_id in ("PAY-003", "PAY-019"):
            matches = [row for row in self.raw if row["payment_id"] == payment_id]
            self.assertEqual(matches[0], matches[1])
        tickets = [p for p in self.report.payments if p.reference.startswith("TICKET-")]
        self.assertEqual(len(tickets), 30)
        self.assertTrue(all(p.amount == Decimal("150") and p.recipient == FUND for p in tickets))
        oliver_tickets = [p for p in tickets if p.sender == "Oliver Falk"]
        self.assertEqual({p.payment_id for p in oliver_tickets}, {"PAY-008", "PAY-030"})
        self.assertIn("friend Robin", oliver_tickets[1].message)

    def test_controlled_messiness_is_present_and_preserved(self) -> None:
        self.assertTrue(any(row["sender"] != row["sender"].strip() for row in self.raw))
        self.assertTrue(any(row["recipient"] != row["recipient"].strip() for row in self.raw))
        self.assertTrue({"completed", "COMPLETED", "Completed", "Pending"}
                        .issubset({row["status"] for row in self.raw}))
        self.assertTrue(any("," in row["amount_dkk"] for row in self.raw))
        self.assertTrue(any("." in row["amount_dkk"] for row in self.raw))
        self.assertEqual([row["payment_id"] for row in self.raw if not row["message"]], ["PAY-028"])
        self.assertIn("PAY-028", {p.payment_id for p in self.report.payments})
        original = [row.copy() for row in self.raw]
        clean_payments(self.raw)
        self.assertEqual(self.raw, original)

    def test_receipt_reconciliation_and_deposit_direction(self) -> None:
        receipts = load_csv(DATA / "receipts.csv")
        self.assertEqual(len(receipts), 6)
        self.assertEqual(len({r["receipt_id"] for r in receipts}), 6)
        self.assertEqual(len({r["reference"] for r in receipts}), 6)
        paid_references = {r["reference"] for r in receipts if r["status"] == "paid"}
        self.assertEqual(set(self.report.spending_by_reference), paid_references)
        speaker = [p for p in self.report.payments if p.reference == "SPEAKER-01"]
        self.assertEqual(len(speaker), 1)
        self.assertEqual((speaker[0].sender, speaker[0].recipient), (FUND, "Oliver Falk"))
        speaker_receipt = next(r for r in receipts if r["reference"] == "SPEAKER-01")
        self.assertEqual((speaker_receipt["buyer"], speaker_receipt["vendor"]),
                         ("Oliver Falk", "Sound Sprout"))
        self.assertFalse(any(p.reference == "DJ-01" for p in self.report.payments))
        flamingos = [p for p in self.report.payments if p.reference == "FLAMINGOS-01"]
        self.assertEqual(len(flamingos), 2)
        self.assertEqual({p.status for p in flamingos}, {"completed", "pending"})

    def test_chat_timing_does_not_reveal_numeric_verdict(self) -> None:
        chat = load_csv(DATA / "chat.csv")
        self.assertTrue(10 <= len(chat) <= 12)
        self.assertTrue(all(datetime.fromisoformat(r["timestamp"]) <= CUTOFF for r in chat))
        text = " ".join(row["message"] for row in chat)
        self.assertIn("16 June", text)
        self.assertIn("13 June", text)
        self.assertIn("reimbursed me", text)
        self.assertIn("still holds the deposit", text)
        self.assertNotRegex(text, r"\b(?:2[,. ]?130|370|5[,. ]?000|2[,. ]?870)\b")
        receipts = load_csv(DATA / "receipts.csv")
        dj = next(r for r in receipts if r["reference"] == "DJ-01")
        self.assertEqual(dj["expected_date"], "2026-06-12")

    def test_money_parsing_and_explicit_bad_input_failures(self) -> None:
        for value in ("150.00", "150,00", " 150,00 "):
            with self.subTest(value=value):
                self.assertEqual(parse_money(value), Decimal("150"))
        for value in ("", "not money", "NaN", "Infinity", "-1", "0", "1.001"):
            with self.subTest(value=value):
                with self.assertRaises((ValueError, InvalidOperation)):
                    parse_money(value)

    def test_conflicting_duplicates_are_not_silently_removed(self) -> None:
        conflict = dict(self.raw[0], amount_dkk="999.00")
        with self.assertRaisesRegex(ValueError, "Conflicting duplicate"):
            clean_payments([self.raw[0], conflict])

    def test_invalid_payments_are_not_silently_ignored(self) -> None:
        for changes in (
            {"status": "cancelled"},
            {"sender": FUND, "recipient": FUND},
            {"recipient": "Not the fund"},
            {"payment_id": ""},
            {"reference": ""},
            {"timestamp": "2026-06-12T10:00:00"},
        ):
            with self.subTest(changes=changes):
                with self.assertRaises(ValueError):
                    clean_payments([dict(self.raw[0], **changes)])

    def test_broken_csv_structure_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "broken.csv"
            for content in ("a,a\n1,2\n", "a,b\n1,2,3\n", "a,b\n1\n"):
                with self.subTest(content=content):
                    path.write_text(content, encoding="utf-8")
                    with self.assertRaises(ValueError):
                        load_csv(path)


class StudentMaterialsTests(unittest.TestCase):
    def test_notebook_is_clean_and_syntax_valid(self) -> None:
        notebook = json.loads((ROOT / "notebooks/festival-investigation.ipynb").read_text())
        self.assertEqual(notebook["nbformat"], 4)
        for number, cell in enumerate(notebook["cells"]):
            if cell["cell_type"] == "code":
                self.assertIsNone(cell["execution_count"])
                self.assertEqual(cell["outputs"], [])
                compile("".join(cell["source"]), f"cell-{number}", "exec")
        source = json.dumps(notebook)
        self.assertIn("TODO", source)
        self.assertNotRegex(source, r"\b(?:2130|2870|370|5000)\b")

    def test_student_pack_allowlist_and_readme_links(self) -> None:
        expected = {
            "README.md", "requirements.txt",
            "data/payments.csv", "data/receipts.csv", "data/chat.csv",
            "docs/student-brief.md", "docs/hints.md",
            "notebooks/festival-investigation.ipynb",
        }
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "student.zip"
            build_pack(destination)
            with ZipFile(destination) as archive:
                self.assertEqual(set(archive.namelist()), expected)
                self.assertIsNone(archive.testzip())
                for source in ("README.md", "docs/student-brief.md", "docs/hints.md"):
                    text = archive.read(source).decode("utf-8")
                    for target in re.findall(r"\]\(([^)]+)\)", text):
                        self.assertIn(target, expected)
                self.assertEqual(archive.read("data/payments.csv"),
                                 (DATA / "payments.csv").read_bytes())
            with self.assertRaises(FileExistsError):
                build_pack(destination)

    def test_scaffold_executes_from_both_student_launch_directories(self) -> None:
        runner = (
            "import json; from pathlib import Path; "
            "root = Path.cwd() if (Path.cwd() / 'data').is_dir() else Path.cwd().parent; "
            "book = json.loads((root / 'notebooks/festival-investigation.ipynb').read_text()); "
            "namespace = {}; "
            "[exec(compile(''.join(cell['source']), 'student-cell', 'exec'), namespace) "
            "for cell in book['cells'] if cell['cell_type'] == 'code']; "
            "assert len(namespace['payments_raw']) == 39; "
            "assert len(namespace['receipts']) == 6; "
            "assert len(namespace['chat']) == 11"
        )
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "student.zip"
            build_pack(destination)
            extracted = Path(directory) / "extracted"
            with ZipFile(destination) as archive:
                archive.extractall(extracted)
            for cwd in (extracted, extracted / "notebooks"):
                with self.subTest(cwd=cwd):
                    result = subprocess.run(
                        [sys.executable, "-c", runner], cwd=cwd,
                        capture_output=True, text=True, check=True,
                    )
                    self.assertIn("Payment rows: 39", result.stdout)
                    self.assertNotIn("FACILITATOR", result.stdout)


if __name__ == "__main__":
    unittest.main()
