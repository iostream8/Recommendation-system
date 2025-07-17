# 🎬 Movie Recommender System

An interactive content-based movie recommender app built using **Python**, **Streamlit**, and **The Movie Database (TMDB) API**.

This project suggests movies similar to the one selected by the user, using dynamic poster fetching from TMDB.

---
## 📌 Features

- 🎥 Recommend 5 similar movies based on selected title
- 🖼️ Displays movie posters dynamically from TMDB
- ⚡ Fast, responsive, and interactive UI via Streamlit
- 📦 Clean code with API error handling and caching

---

## 🧠 How It Works

1. Loads a dataset (`movies.pkl`) with movie titles and TMDB IDs
2. Uses a precomputed similarity matrix (`similarity.pkl`)
3. Recommends top 5 similar movies based on cosine similarity
4. Fetches posters using the TMDB API

---

## 🛠️ Tech Stack

- **Python 3.8+**
- **Pandas**
- **Pickle**
- **Requests**
- **Streamlit**
- **TMDB API**

---

## 🧰 Setup Instructions

### 1. Clone the repo

```bash
git clone https://https://github.com/iostream8/Recommendation-system
cd Recommendation-system

---
##📁 Project Structure
Recommendation-system/
│
├── app.py                  # Streamlit application
├── movies.pkl              # Preprocessed movie metadata with TMDB IDs
├── similarity.pkl          # Precomputed similarity matrix
|── tmdb_5000_credits.csv   # CSV file

