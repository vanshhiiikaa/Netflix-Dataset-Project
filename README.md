# Netflix Dataset Analysis 🎬

A Python data analysis project exploring Netflix content data using **Pandas** and **Matplotlib** — covering data cleaning, and visualizing content type distribution, ratings, and movie durations.

## 📌 About The Project

This project analyzes a Netflix titles dataset to uncover patterns in the platform's content: what proportion is Movies vs. TV Shows, how content ratings are distributed, and how long Netflix movies typically run.

## ✨ Features

- **Data Cleaning** — removes rows with missing values in key columns (cast, country, date added, rating, duration) using Pandas
- **Content Type Distribution** — bar chart comparing Movies vs. TV Shows
- **Ratings Distribution** — pie chart showing the breakdown of content ratings (e.g., TV-MA, PG-13, R)
- **Movie Duration Analysis** — histogram of movie runtimes, with duration values cleaned and converted from text to numeric minutes

## 📸 Screenshots

<!-- Add your chart outputs here -->
| Analysis | Preview |
|---|---|
| Content Type Distribution (Bar Chart) | ![Content type bar chart](screenshots/content_type.png) |
| Ratings Distribution (Pie Chart) | ![Ratings pie chart](screenshots/ratings.png) |
| Movie Duration Distribution (Histogram) | ![Movie duration histogram](screenshots/duration.png) |

> To add these: run `netflix.py`, screenshot each chart window as it appears, create a `screenshots/` folder in this repo, upload the images, and match the filenames above.

## Dataset

`netflix_subset.csv` — a subset of Netflix titles data including columns like `type`, `cast`, `country`, `date_added`, `rating`, and `duration`.

## How It Works

1. Loads the dataset using `pandas.read_csv()`
2. Drops rows with missing values in critical columns to ensure clean analysis
3. Uses `value_counts()` to summarize content types and ratings
4. Plots:
   - A **bar chart** of content type counts
   - A **pie chart** of rating distribution with percentage labels
   - A **histogram** of movie durations (after cleaning the "min" text suffix and converting to integers)

## Getting Started

### Prerequisites
- Python 3.x
- Pandas (`pip install pandas`)
- Matplotlib (`pip install matplotlib`)

### Installation
```bash
git clone https://github.com/vanshhiiikaa/Netflix-Dataset-Project.git
cd Netflix-Dataset-Project
```

### Usage
```bash
python netflix.py
```
This will display three charts in sequence: content type distribution, ratings distribution, and movie duration distribution.

## Tech Stack
- Python 3
- Pandas (data loading and cleaning)
- Matplotlib (data visualization)

## Possible Improvements
- [ ] Add analysis of content added over time (trend by year/month using `date_added`)
- [ ] Break down ratings by content type (Movies vs. TV Shows separately)
- [ ] Add country-wise content distribution analysis
- [ ] Save generated charts as image files automatically
- [ ] Turn into a Jupyter Notebook with markdown explanations alongside each chart
- [ ] Add basic statistical summary (mean/median movie duration, etc.)

## Author
**Vanshika**
- GitHub: [@vanshhiiikaa](https://github.com/vanshhiiikaa)
- LinkedIn: [Vanshika Gupta](https://www.linkedin.com/in/vanshika-gupta-4a2002329)

## License
This project is open source and available under the [MIT License](LICENSE).
