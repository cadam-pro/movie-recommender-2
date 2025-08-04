from fastapi import FastAPI

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
