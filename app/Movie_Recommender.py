import ast
import streamlit as st
import pandas as pd
import requests

st.set_page_config(layout="wide")
st.title("🎬 Recommandation de films")


@st.cache_data
def load_data():
    return pd.read_csv("data/TMDB_clean.csv")


df = load_data()

movie_titles = ["--- Sélectionne un film ---"] + df["title"].tolist()

selected_title = st.selectbox(
    "Choisis un film pour obtenir des recommandations",
    movie_titles,
    index=0,  # Par défaut, la première option
)

if selected_title != "--- Sélectionne un film ---":
    # --- Récupérer l'ID correspondant ---
    selected_row = df[df["title"] == selected_title]
    if not selected_row.empty:
        movie_id = selected_row.iloc[0]["id"]

        # --- Appel à l'API ---
        response = requests.get(
            f"http://backend:8000/recommendations?movie_id={movie_id}"
        )
        if response.status_code == 200:
            movies = response.json()

            # --- Fonction d'affichage des infos ---

            def display_movie(movie_json, label):
                # Convertir certaines colonnes de str -> list
                list_cols = [
                    "genres_array",
                    "production_countries_array",
                    "director_array",
                ]

                if not isinstance(movie_json, dict):
                    st.error(f"⚠️ Film invalide reçu : {selected_title} #{movie_id}")
                    return

                data = movie_json

                for col in list_cols:
                    if col in data and isinstance(data[col], str):
                        try:
                            data[col] = ast.literal_eval(data[col])
                        except Exception:
                            data[col] = []

                st.subheader(f"{label} : {data['title']}")
                cols = st.columns([1, 2])
                with cols[0]:
                    st.image(
                        f"https://image.tmdb.org/t/p/w500{data['poster_path']}",
                        width=300,
                    )
                with cols[1]:
                    st.markdown(f"**Overview** : {data.get('overview', '')}")
                    st.markdown(
                        f"**Réalisateur(s)** : {', '.join(data.get('director_array', []))}"
                    )
                    st.markdown(f"**Note moyenne** : {data.get('vote_average', 'N/A')}")
                    st.markdown(
                        f"**Date de sortie** : {data.get('release_date', 'N/A')}"
                    )
                    st.markdown(
                        f"**Durée** : {int(float(data['runtime'])) if data.get('runtime') else 'N/A'} minutes"
                    )
                    st.markdown(
                        f"**Genres** : {', '.join(data.get('genres_array', []))}"
                    )
                    st.markdown(
                        f"**Pays de production** : {', '.join(data.get('production_countries_array', []))}"
                    )

            # --- Affichage des recommandations ---
            st.markdown("## 📌 Recommandations")
            # For each film in recommendations, display its info
            for i, movie in enumerate(movies, 1):
                display_movie(movie, f"Recommandation #{i}")
        else:
            st.error("Erreur lors de la récupération des recommandations.")
