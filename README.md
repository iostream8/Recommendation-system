# 🎬 Movie Recommendation System

A simple content-based movie recommender built using Python and Streamlit. It suggests movies based on a given movie title using data from the TMDB 5000 dataset.

---

## 📑 Table of Contents

- [📌 Competition Overview](#competition-overview)
- [📊 Dataset](#dataset)
- [📁 Files Included](#files-included)
- [📈 Results](#results)
- [⚙️ Approach Summary](#approach-summary)
- [🚀 How to Use](#how-to-use)
- [📬 Contact](#contact)

---

## 📌 Competition Overview

This project aims to build a movie recommendation system using **content-based filtering**. It uses metadata such as genres, keywords, cast, and crew to compute movie similarity and recommend the top 5 similar movies to a given input title.

---

## 📊 Dataset

The data used in this project comes from the popular [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).

**Key Files:**
- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

---

## 📁 Files Included

| File | Description |
|------|-------------|
| `app.py` | Streamlit app to run the recommender system |
| `Recommender_system.ipynb` | Jupyter notebook with full EDA and model creation |
| `similarity.pkl` | Precomputed similarity matrix (⚠️ Not included in GitHub due to file size limit) |
| `.gitignore` | Ignore unnecessary or large files (e.g., `.pkl`, `.venv`, `.csv`) |
| `tmdb_5000_movies.csv`, `tmdb_5000_credits.csv` | Datasets used to build the model |

---

## 📈 Results

The recommender system returns top 5 similar movies with their poster images. It performs well for most mainstream movie titles and uses cosine similarity on combined features for content matching.

---

## ⚙️ Approach Summary

1. **Data Preprocessing**:
   - Merged movies and credits datasets
   - Extracted keywords, genres, cast, crew (only director), and overview

2. **Feature Engineering**:
   - Converted text features into lowercase and removed spaces
   - Combined all relevant features into a single `"tags"` column

3. **Vectorization**:
   - Used `CountVectorizer` to convert text data to numerical vectors

4. **Similarity Matrix**:
   - Used **Cosine Similarity** to compute similarity between all movies
   - Saved the matrix as `similarity.pkl` for fast lookup

5. **Streamlit App**:
   - Takes a movie name as input
   - Displays top 5 recommendations with their posters from TMDB API

---

## 🚀 How to Use

### 1. Clone the repo

```bash
git clone https://github.com/iostream8/Recommendation-system.git
cd Recommendation-system
