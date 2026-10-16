
"""Validate the Netflix dataset without overwriting the original CSV."""

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "netflix_subset.csv"

REQUIRED_COLUMNS = {
    "type",
    "rating",
    "duration",
}


def main():
    if not DATA_FILE.exists():
        print(f"ERROR: Dataset not found: {DATA_FILE.name}")
        print("Upload netflix_subset.csv to the repository root.")
        return

    try:
        data = pd.read_csv(DATA_FILE)
    except (OSError, pd.errors.ParserError, UnicodeDecodeError) as error:
        print(f"ERROR: Could not read the CSV: {error}")
        return

    data.columns = data.columns.str.strip().str.lower()

    print("=" * 45)
    print("       NETFLIX DATASET VALIDATOR")
    print("=" * 45)

    print(f"\nFile: {DATA_FILE.name}")
    print(f"Rows: {len(data)}")
    print(f"Columns: {len(data.columns)}")
    print(f"\nColumn names: {', '.join(data.columns)}")

    missing_columns = REQUIRED_COLUMNS - set(data.columns)

    if missing_columns:
        print(f"\nERROR: Missing columns: {sorted(missing_columns)}")
        print("Please check the CSV header.")
        return

    print("\nContent type counts:")
    print(data["type"].fillna("Unknown").value_counts().to_string())

    print("\nMissing values by column:")
    print(data.isna().sum().to_string())

    print(f"\nDuplicate rows: {data.duplicated().sum()}")

    print("\nDataset validation completed.")
    print("Original CSV was not modified.")


if __name__ == "__main__":
    main()
