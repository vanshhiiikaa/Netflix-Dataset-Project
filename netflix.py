
"""
Netflix Dataset Analysis
Analyzes content types, ratings, movie durations,
countries, and content added over time.
"""

from pathlib import Path

import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "netflix_subset.csv"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

# Load data
if not DATA_FILE.exists():
    raise FileNotFoundError(
        "netflix_subset.csv nahi mili. "
        "CSV file ko netflix.py ke saath rakho."
    )

df = pd.read_csv(DATA_FILE)
df.columns = df.columns.str.strip().str.lower()

# Validate required columns
required = {"type", "rating", "duration"}
missing = required - set(df.columns)

if missing:
    raise ValueError(f"Required columns missing: {sorted(missing)}")

# Clean text and duplicates
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

df = df.drop_duplicates().copy()

for col in ["type", "rating", "duration"]:
    df[col] = df[col].fillna("Unknown")

print("=" * 45)
print("       NETFLIX DATASET ANALYSIS")
print("=" * 45)
print(f"\nTotal records: {len(df)}")
print("\nContent types:")
print(df["type"].value_counts().to_string())
print("\nRatings:")
print(df["rating"].value_counts().to_string())
print("\nMissing values:")
print(df.isna().sum().to_string())

def save_chart(filename):
    """Save the current chart and release memory."""
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / filename, dpi=150, bbox_inches="tight")
    plt.close()

# 1. Movies vs TV Shows
type_counts = df["type"].value_counts()

plt.figure(figsize=(8, 5))
type_counts.plot(kind="bar", color=["#E50914", "#555555"])
plt.title("Netflix Content Type Distribution")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")
plt.xticks(rotation=0)
save_chart("content_types.png")

# 2. Ratings distribution
rating_counts = df["rating"].value_counts().head(15)

plt.figure(figsize=(10, 6))
rating_counts.sort_values().plot(
    kind="barh", color="#E50914"
)
plt.title("Top Netflix Ratings")
plt.xlabel("Number of Titles")
plt.ylabel("Rating")
save_chart("ratings_distribution.png")

# 3. Movie duration
movies = df[df["type"].str.casefold() == "movie"].copy()

movies["duration_minutes"] = pd.to_numeric(
    movies["duration"].str.extract(r"(\d+)\s*min", expand=False),
    errors="coerce"
)

durations = movies["duration_minutes"].dropna()

if not durations.empty:
    print("\nMovie duration statistics:")
    print(f"Average: {durations.mean():.1f} minutes")
    print(f"Median: {durations.median():.1f} minutes")
    print(f"Shortest: {durations.min():.0f} minutes")
    print(f"Longest: {durations.max():.0f} minutes")

    plt.figure(figsize=(9, 5))
    plt.hist(durations, bins=15, color="#E50914", edgecolor="white")
    plt.title("Netflix Movie Duration Distribution")
    plt.xlabel("Duration (minutes)")
    plt.ylabel("Number of Movies")
    save_chart("movie_durations.png")
else:
    print("\nNo valid movie durations found.")

# 4. Country distribution (if available)
if "country" in df.columns:
    countries = (
        df["country"].dropna()
        .str.split(",")
        .explode()
        .str.strip()
    )
    countries = countries[
        (countries != "") & (countries != "Unknown")
    ]
    top_countries = countries.value_counts().head(10)

    if not top_countries.empty:
        plt.figure(figsize=(10, 6))
        top_countries.sort_values().plot(
            kind="barh", color="#B20710"
        )
        plt.title("Top 10 Countries by Title Count")
        plt.xlabel("Count")
        plt.ylabel("Country")
        save_chart("top_countries.png")

# 5. Content added by year (if available)
if "date_added" in df.columns:
    dates = pd.to_datetime(df["date_added"], errors="coerce")
    yearly = dates.dropna().dt.year.value_counts().sort_index()

    if not yearly.empty:
        plt.figure(figsize=(10, 5))
        yearly.plot(kind="line", marker="o", color="#E50914")
        plt.title("Netflix Titles Added by Year")
        plt.xlabel("Year")
        plt.ylabel("Titles Added")
        plt.grid(alpha=0.25)
        save_chart("titles_added_by_year.png")

# Export cleaned data and summary
df.to_csv(OUTPUT_DIR / "netflix_cleaned.csv", index=False)

summary = pd.DataFrame({
    "metric": ["Total records", "Movies", "TV Shows", "Duplicate rows removed"],
    "value": [
        len(df),
        int((df["type"].str.casefold() == "movie").sum()),
        int((df["type"].str.casefold() == "tv show").sum()),
        "See commit history / original data"
    ]
})
summary.to_csv(OUTPUT_DIR / "summary.csv", index=False)

print(f"\nCleaned dataset and charts saved in: {OUTPUT_DIR}")
print("Analysis completed successfully.")
print("Charts are saved as PNG files; no display window is required.")
