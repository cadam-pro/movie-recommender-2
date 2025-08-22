from sklearn.feature_extraction.text import TfidfVectorizer
import umap.umap_ as umap
import numpy as np
import pandas as pd


def train_model(df: pd.DataFrame) -> pd.DataFrame:
    """Train a UMAP model on the movie plot summaries."""
    # Vectorisation TF-IDF sur les résumés
    vectorizer = TfidfVectorizer(max_features=1000, stop_words="english")
    X_tfidf = vectorizer.fit_transform(df["overview"])

    # Réduction dimensionnelle avec UMAP
    reducer = umap.UMAP(
        n_neighbors=15,
        min_dist=0.1,
        n_components=2,
        metric="cosine",
        init="spectral",
        random_state=42,
    )
    embedding = reducer.fit_transform(X_tfidf.toarray())

    df["x"] = embedding[:, 0]
    df["y"] = embedding[:, 1]
    print("Model trained and embeddings added to DataFrame.")
    return df


def find_closest_movies(df, movie_id, top_n=10):
    """Find the closest movies to a given movie ID based on UMAP embeddings."""
    if movie_id not in df["id"].values:
        print(f"Le film '{movie_id}' n'a pas été trouvé.")
        return None

    input_point = df.loc[df["id"] == movie_id, ["x", "y"]].values[0]
    df["distance"] = np.linalg.norm(df[["x", "y"]].values - input_point, axis=1)

    df_filtered = df[df["id"] != movie_id]
    closest_movies = df_filtered.nsmallest(top_n, "distance")

    return closest_movies[
        [
            "id",
            "title",
            "vote_average",
            "vote_count",
            "release_date",
            "runtime",
            "overview",
            "popularity",
            "poster_path",
            "genres_array",
            "production_countries_array",
            "production_companies_array",
            "cast_array",
            "director_array",
            "writers_array",
            "distance",
        ]
    ]
