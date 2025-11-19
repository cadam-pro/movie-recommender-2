import pandas as pd
from data import sort_df, convert_types, clean_data


def test_sort_df():
    df = pd.DataFrame(
        {"vote_count": [1, 10, 5], "popularity": [1, 3, 2], "vote_average": [7, 8, 6]}
    )
    out = sort_df(df)
    assert out.iloc[0]["vote_count"] == 10


def test_convert_types():
    df = pd.DataFrame(
        {
            "vote_average": ["7.5"],
            "vote_count": ["10"],
            "runtime": ["120"],
            "budget": ["1000"],
            "popularity": ["5.2"],
            "release_date": ["2000-01-01"],
            "genres": ["Drama, Comedy"],
            "production_countries": ["USA, France"],
            "production_companies": ["A, B"],
            "cast": ["X, Y"],
            "director": ["Z"],
            "writers": ["W"],
            # colonnes supprimées
            "status": [""],
            "imdb_id": [""],
            "tagline": [""],
            "director_of_photography": [""],
            "producers": [""],
            "imdb_rating": [""],
            "imdb_votes": [""],
            "music_composer": [""],
            "revenue": [""],
            "spoken_languages": [""],
            "original_language": [""],
        }
    )
    out = convert_types(df)
    assert out["vote_count"].dtype.name == "Int64"
    assert out["release_year"].iloc[0] == 2000
    assert out["genres_array"].iloc[0] == ["Drama", "Comedy"]
    assert "genres" not in out.columns
    assert "status" not in out.columns
    assert "imdb_id" not in out.columns
    assert "tagline" not in out.columns
    assert "director_of_photography" not in out.columns
    assert "producers" not in out.columns
    assert "imdb_rating" not in out.columns
    assert "imdb_votes" not in out.columns
    assert "music_composer" not in out.columns
    assert "revenue" not in out.columns
    assert "spoken_languages" not in out.columns
    assert "original_language" not in out.columns
    assert out["vote_average"].dtype == float
    assert out["runtime"].dtype == float
    assert out["budget"].dtype == float
    assert out["popularity"].dtype == float
    assert out["production_countries_array"].iloc[0] == ["USA", "France"]
    assert out["production_companies_array"].iloc[0] == ["A", "B"]
    assert out["cast_array"].iloc[0] == ["X", "Y"]
    assert out["director_array"].iloc[0] == ["Z"]
    assert out["writers_array"].iloc[0] == ["W"]
    assert "production_countries" not in out.columns
    assert "production_companies" not in out.columns
    assert "cast" not in out.columns
    assert "director" not in out.columns
    assert "writers" not in out.columns


def test_clean_data():
    df = pd.DataFrame(
        {
            "title": ["ok", "", None],
            "overview": ["ok", None, ""],
            "release_year": [None, 2020, 2021],
            "runtime": [50, 30, 60],
            "genres_array": [["Drama"], ["Documentary"], ["Comedy"]],
        }
    )
    out = clean_data(df)
    assert all(out["runtime"] > 44)
    assert "Documentary" not in sum(out["genres_array"], [])
    assert out["release_year"].iloc[0] is not None
    assert out["release_year"].iloc[0] == -1
