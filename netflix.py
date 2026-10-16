
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# Project folders
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "netflix_subset.csv"
OUTPUT_DIR = BASE_DIR / "output"

OUTPUT_DIR.mkdir(exist_ok=True)

# Load dataset
if not DATA_FILE.exists():
    raise FileNotFoundError(
        f"Dataset not found: {DATA_FILE}\n"
        "Please keep netflix_subset.csv beside netflix.py."
    )

data = pd.read_csv(DATA_FILE)

# Normalize column names and text values
data.columns = data.columns.str.strip().str.lower()

required_columns = {"type", "rating", "duration"}
missing_columns = required_columns - set(data.columns)

if missing_columns:
    raise ValueError(
        f"Missing required columns: {sorted(missing_columns)}"
    )

for column in data.select_dtypes(include="object").columns:
    data[column] = data[column].str.strip()

# Remove duplicate rows
data = data.drop_duplicates().copy()

# Handle missing values without deleting entire records unnecessarily
data["type"] = data["type"].fillna("Unknown")
data["rating"] = data["rating"].fillna("Not Rated")
data["duration"] = data["duration"].fillna("")

print("\n===== NETFLIX DATASET SUMMARY =====")
print(f"Total records: {len(data)}")
print("\nContent type counts:")
print(data["type"].value_counts())

print("\nMissing values per column:")
print(data.isna().sum())

# 1. Content type distribution
type_counts = data["type"].value_counts()

if not type_counts.empty:
    fig, ax = plt.subplots(figsize=(8, 5))
    type_counts.plot(
        kind="bar",
        ax=ax,
        color=["#E50914", "#564D4D", "#808080"]
    )
    ax.set_title("Netflix Content Type Distribution")
    ax.set_xlabel("Content Type")
    ax.set_ylabel("Number of Titles")
    ax.tick_params(axis="x", rotation=0)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "content_types.png", dpi=150)
    plt.show()
    plt.close(fig)

# 2. Ratings distribution
rating_counts = data["rating"].value_counts()

if not rating_counts.empty:
    fig, ax = plt.subplots(figsize=(10, 6))
    rating_counts.plot(
        kind="bar",
        ax=ax,
        color="#E50914"
    )
    ax.set_title("Netflix Ratings Distribution")
    ax.set_xlabel("Rating")
    ax.set_ylabel("Number of Titles")
    ax.tick_params(axis="x", rotation=45)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "ratings_distribution.png", dpi=150)
    plt.show()
    plt.close(fig)

# 3. Movie duration analysis
movies = data.loc[
    data["type"].str.casefold() == "movie"
].copy()

movies["duration_minutes"] = pd.to_numeric(
    movies["duration"].str.extract(r"(\d+)\s*min", expand=False),
    errors="coerce"
)

movie_durations = movies["duration_minutes"].dropna()

if not movie_durations.empty:
    print("\n===== MOVIE DURATION STATISTICS =====")
    print(f"Movies with numeric duration: {len(movie_durations)}")
    print(f"Average duration: {movie_durations.mean():.1f} minutes")
    print(f"Median duration: {movie_durations.median():.1f} minutes")
    print(f"Shortest duration: {movie_durations.min():.0f} minutes")
    print(f"Longest duration: {movie_durations.max():.0f} minutes")

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.hist(
        movie_durations,
        bins=20,
        color="#E50914",
        edgecolor="white"
    )
    ax.set_title("Netflix Movie Duration Distribution")
    ax.set_xlabel("Duration (minutes)")
    ax.set_ylabel("Number of Movies")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "movie_durations.png", dpi=150)
    plt.show()
    plt.close(fig)
else:
    print("\nNo valid movie durations found in the dataset.")

# 4. Save cleaned data
cleaned_file = OUTPUT_DIR / "netflix_cleaned.csv"
data.to_csv(cleaned_file, index=False, encoding="utf-8")

print(f"\nCleaned dataset saved to: {cleaned_file}")
print(f"Charts saved in: {OUTPUT_DIR}")
print("\nAnalysis completed successfully!")
