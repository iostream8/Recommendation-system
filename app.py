import streamlit as st
import pickle
import pandas as pd
import requests
import time

# --- Load Data ---
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# --- TMDB API Key ---
api_key = '8a545070768a5c66e97abe40fbca833a'

# --- Fetch poster by movie ID ---
@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get("poster_path")
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return "https://via.placeholder.com/300x450?text=No+Image"
    except Exception as e:
        print(f"[ERROR] Failed for movie_id {movie_id}: {e}")
        return "https://via.placeholder.com/300x450?text=No+Image"

# --- Fallback: Fetch poster by movie title ---
@st.cache_data(show_spinner=False)
def fetch_poster_by_title(title):
    try:
        url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={title}"
        response = requests.get(url, timeout=5)
        data = response.json()
        if data['results']:
            poster_path = data['results'][0].get('poster_path')
            if poster_path:
                return "https://image.tmdb.org/t/p/w500/" + poster_path
    except Exception as e:
        print(f"[ERROR] Failed for title '{title}': {e}")
    return "https://via.placeholder.com/300x450?text=No+Image"

# --- Recommendation Function ---
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(
        list(enumerate(distances)), reverse=True, key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movie_list:
        title = movies.iloc[i[0]]['title']
        movie_id = movies.iloc[i[0]].get('movie_id')

        recommended_movies.append(title)

        # Try fetch by ID first
        poster = fetch_poster(movie_id)
        if "placeholder" in poster:  # fallback if poster is broken
            poster = fetch_poster_by_title(title)

        recommended_posters.append(poster)

        time.sleep(0.3)  # avoid rate-limiting

    return recommended_movies, recommended_posters

# --- Streamlit UI ---
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title("🎬 Movie Recommender System")
st.markdown("Pick a movie you like and we'll recommend 5 others.")

selected_movie = st.selectbox("Choose a movie:", movies['title'].values)

if st.button("Recommend"):
    names, posters = recommend(selected_movie)

    st.subheader("Here are your recommendations:")
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.markdown(f"**{names[i]}**")
            st.image(posters[i])
