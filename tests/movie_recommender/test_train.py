import pandas as pd
import numpy as np
from train import train_model, find_closest_movies


def test_train_model(monkeypatch):
    df = pd.DataFrame({"overview": ["plot1", "plot2", "plot3"]})

    class DummyUMAP:
        def fit_transform(self, X):
            return np.array([[0, 0], [1, 1], [2, 2]])

    monkeypatch.setattr("train.umap.UMAP", lambda *a, **k: DummyUMAP())

    out = train_model(df)
    assert "x" in out.columns and "y" in out.columns
    assert len(out) == 3


def test_find_closest_movies():
    df = pd.DataFrame(
        {
            "id": [1, 2, 3],
            "title": ["A", "B", "C"],
            "vote_average": [7, 8, 6],
            "vote_count": [10, 20, 5],
            "release_date": ["2020", "2021", "2019"],
            "runtime": [100, 120, 90],
            "overview": ["plot1", "plot2", "plot3"],
            "popularity": [5, 6, 4],
            "poster_path": ["p1", "p2", "p3"],
            "genres_array": [["Drama"], ["Comedy"], ["Action"]],
            "production_countries_array": [["US"], ["FR"], ["US"]],
            "production_companies_array": [["A"], ["B"], ["C"]],
            "cast_array": [["X"], ["Y"], ["Z"]],
            "director_array": [["D1"], ["D2"], ["D3"]],
            "writers_array": [["W1"], ["W2"], ["W3"]],
            "x": [0, 1, 2],
            "y": [0, 1, 2],
        }
    )
    closest = find_closest_movies(df, 1, top_n=2)
    assert closest.shape[0] == 2
    assert 1 not in closest["id"].values
