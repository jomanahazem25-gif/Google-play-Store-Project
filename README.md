# Google-play-Store-Project
Epsilon AI Data analysis Final Project
 Google Play Store — Data Analysis

Exploratory analysis of the Google Play Store dataset. The project covers data cleaning, answering 10 research questions through visualisations, and an interactive Streamlit dashboard.

---

## What's in this repo

Google_Play_Store_Project.ipynb       # main analysis notebook
app.py                                # Streamlit dashboard
googleplaystore.csv                   # app metadata (10,841 rows) googleplaystore_user_reviews.csv 
requirements.txt
README.md
```

---

## The dataset

CSV file from [Kaggle](https://www.kaggle.com/datasets/lava18/google-play-store-apps):

- **googleplaystore.csv** — app name, category, rating, reviews, size, installs, type, price, content rating, genres, last updated, android version
- **googleplaystore_user_reviews.csv** — translated reviews with sentiment polarity and subjectivity scores

The data is intentionally messy — size values like `"19M"`, installs like `"10,000+"`, prices like `"$4.99"` — cleaning it is part of the work.

---

## Data cleaning


- `Installs` | String with `,` and `+` | Strip symbols, cast to int |
- `Price` | String with `$` | Strip symbol, cast to float |
- `Reviews` | Some values had `M` suffix | Strip M, cast to int |
- `Size` | Mix of `"19M"`, `"512k"`, `"Varies with device"` | Custom `clean_size()` function → float MB |
- `Last Updated` | Plain string | Parsed with `pd.to_datetime` |
- `Android Ver` | `"4.1 and up"` style strings | Regex extract of the version number |
- `Rating` | 1,474 nulls | Filled with median |
- `Type` | 1 null | Filled with mode (Free) |
- Duplicates | 483 duplicate rows | Dropped |

---

## Research questions

| # Question | Type |

| Q1 | Which categories have the most apps? | Univariate |
| Q2 | What is the distribution of app ratings? | Univariate |
| Q3 | Does price affect the rating? | Bivariate |
| Q4 | Are most apps Free or Paid? | Univariate |
| Q5 | Is there a direct correlation between Rating and Installs? | Bivariate |
| Q6 | How does Android version relate to installs? | Bivariate |
| Q7 | Do installs decrease as app size increases? | Bivariate |
| Q8 | Is there a relation between Rating and app size? | Bivariate |
| Q9 | Which categories have the largest number of installs? | Bivariate |
| Q10 | What is the distribution of app sizes? | Univariate |

---

## Key findings

- **Family** is the biggest category by app count, with Game and Tools behind it
- Ratings cluster between **4.0 and 4.5** — the distribution is left-skewed
- **92.6%** of apps are free
- Price barely influences rating — the two are almost uncorrelated
- App size and install count have no meaningful relationship
- **Family and Communication** lead in total installs
- Most apps are in the **2.5–7.4 MB** size range

---

## Running locally

```bash
# 1. clone the repo
git clone https://github.com/YOUR_USERNAME/google-play-store-analysis.git
cd google-play-store-analysis

# 2. install dependencies
pip install -r requirements.txt

# 3. open the notebook
jupyter notebook Google_Play_Store_Project.ipynb

## Streamlit dashboard

The dashboard has four tabs:

- **Univariate** — category distribution, rating histogram, free/paid pie, size histogram, treemap
- **Bivariate** — price vs rating, rating vs installs, android version boxplot, size vs installs, rating vs size


## Requirements

pandas
numpy
plotly
streamlit
jupyter
