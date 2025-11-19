from fastapi import FastAPI
from src.movie_recommender.utils import read_csv
from src.movie_recommender.params import full_path_trained
from src.movie_recommender.train import find_closest_movies

mr_api = FastAPI(
    title="Movie Recommender API 2",
    description="API for the web application : Movie Recommender 2!",
)


@mr_api.get("/")
def read_root():
    """
    Root endpoint of the Web API.
    """
    return {"message": "Welcome to the Web API!"}


@mr_api.get("/recommendations")
def get_recommendations(movie_id: int):
    """
    Endpoint to get movie recommendations based on a given movie ID.
    """
    df = read_csv(full_path_trained)
    recommendations = find_closest_movies(df, movie_id, 5)
    return (
        recommendations.to_dict(orient="records")
        if recommendations is not None
        else {"error": "Movie ID not found"}
    )
