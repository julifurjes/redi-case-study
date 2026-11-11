"""Build a student-only ZIP using an explicit allowlist, without answer keys."""

import argparse
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parents[1]
STUDENT_FILES = (
    ("STUDENT_README.md", "README.md"),
    ("docs/student-brief.md", "docs/student-brief.md"),
    ("docs/hints.md", "docs/hints.md"),
    ("data/payments.csv", "data/payments.csv"),
    ("data/receipts.csv", "data/receipts.csv"),
    ("data/chat.csv", "data/chat.csv"),
    ("notebooks/festival-investigation.ipynb", "notebooks/festival-investigation.ipynb"),
    ("requirements.txt", "requirements.txt"),
)


def build_pack(destination: Path) -> Path:
    for source, _ in STUDENT_FILES:
        if not (ROOT / source).is_file():
            raise FileNotFoundError(ROOT / source)
    destination.parent.mkdir(parents=True, exist_ok=True)
    # Exclusive creation protects any existing archive from accidental replacement.
    with ZipFile(destination, "x", compression=ZIP_DEFLATED) as archive:
        for source, target in STUDENT_FILES:
            archive.write(ROOT / source, arcname=target)
    return destination


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "dist/festival-student-pack.zip")
    args = parser.parse_args()
    print(f"Student pack created: {build_pack(args.output)}")


if __name__ == "__main__":
    main()
