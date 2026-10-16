
# Netflix Dataset Analysis 🎬

A Python data analysis project that explores Netflix movies and TV shows using Pandas and Matplotlib.

## Project Overview

This project analyzes Netflix title data to understand content types, ratings, movie durations, country distribution, and content additions over time.

## Features

- Data validation and cleaning
- Movies vs. TV Shows distribution
- Ratings distribution
- Movie duration statistics
- Top countries by title count
- Titles added by year
- Export of cleaned data and charts

## Project Structure

```text
Netflix-Dataset-Project/
├── netflix.py
├── netflix_titles.py
├── netflix_subset.csv
├── requirements.txt
├── README.md
└── output/
```

The `output/` folder is created automatically when the analysis runs.

## Requirements

- Python 3.9 or later
- Pandas
- Matplotlib

## Installation

Install the required packages:

```bash
python -m pip install -r requirements.txt
```

## How to Run

Run the dataset validator:

```bash
python netflix_titles.py
```

Run the analysis:

```bash
python netflix.py
```

## Output

The analysis generates:

- `content_types.png`
- `ratings_distribution.png`
- `movie_durations.png`
- `top_countries.png` (if country data is available)
- `titles_added_by_year.png` (if date data is available)
- `netflix_cleaned.csv`
- `summary.csv`

All generated files are saved in the `output/` directory.

## Dataset

The project uses `netflix_subset.csv`.

The analysis expects the dataset to contain `type`, `rating`, and `duration` columns. Country and date-added analysis are optional.

## Technologies Used

- Python
- Pandas
- Matplotlib
- CSV

## Notes

The validator does not overwrite the original dataset. The analysis removes duplicate rows from its working copy and handles missing values in key analysis columns.

Generated charts and cleaned data are created when the Python script runs; editing files on GitHub alone does not execute the scripts.

## Author

Vanshika

## License

See the repository license for licensing information.
