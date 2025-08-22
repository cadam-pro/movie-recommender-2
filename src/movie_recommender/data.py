import pandas as pd


def read_csv(filepath: str) -> pd.DataFrame:
    """Read a CSV file and return its contents."""

    return pd.read_csv(filepath)


def sort_df(df: pd.DataFrame) -> pd.DataFrame:
    """Sort a DataFrame by a specified column in descending order."""
    df_sorted = df.sort_values(
        by=["vote_count", "popularity", "vote_average"], ascending=[False, False, False]
    )
    return df_sorted.head(50000).copy()


def convert_types(df: pd.DataFrame) -> pd.DataFrame:
    """Convert DataFrame columns to appropriate data types."""
    # Conversions numériques
    df["vote_average"] = pd.to_numeric(df["vote_average"], errors="coerce").astype(
        float
    )
    df["vote_count"] = pd.to_numeric(df["vote_count"], errors="coerce").astype(
        "Int64"
    )  # Int64 pour accepter NaN
    df["runtime"] = pd.to_numeric(df["runtime"], errors="coerce").astype(float)
    df["budget"] = pd.to_numeric(df["budget"], errors="coerce").astype(float)
    df["popularity"] = pd.to_numeric(df["popularity"], errors="coerce").astype(float)

    # Dates
    df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")
    df["release_year"] = df["release_date"].dt.year.astype("Int64")

    # Colonnes à transformer en listes
    array_columns = [
        "genres",
        "production_countries",
        "production_companies",
        "cast",
        "director",
        "writers",
    ]

    for col in array_columns:
        df[col + "_array"] = (
            df[col]
            .str.split(r",\s*")  # découper sur virgule + espace
            .apply(lambda x: x if isinstance(x, list) else [])  # remplacer NaN par []
        )

    # Suppression des colonnes originales
    df = df.drop(columns=array_columns)

    # Suppression des colonnes inutiles
    return df.drop(
        [
            "status",
            "imdb_id",
            "tagline",
            "director_of_photography",
            "producers",
            "imdb_rating",
            "imdb_votes",
            "music_composer",
            "revenue",
            "spoken_languages",
            "original_language",
        ],
        axis=1,
    )


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean the DataFrame by sorting and converting types."""
    # Delete line with empty title
    df = df[df["title"].notna() & (df["title"] != "")]
    # Delete line with empty overview
    df = df[df["overview"].notna() & (df["overview"] != "")]
    # Fill NaN in release_year with -1
    df = df.fillna({"release_year": -1})
    # Keep only movies with runtime > 44 minutes
    df = df[df["runtime"] > 44.0]
    # Remove documentaries
    return df[
        ~df["genres_array"].apply(lambda x: len(x) == 1 and x[0] == "Documentary")
    ]
