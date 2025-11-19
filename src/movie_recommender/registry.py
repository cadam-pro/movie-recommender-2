from kaggle.api.kaggle_api_extended import KaggleApi
from params import DEST_FILE, full_path_all
from utils import delete_if_file_exists
import pandas as pd


def get_kaggle_csv() -> None:
    """Download the CSV file from Kaggle."""
    delete_if_file_exists(full_path_all)
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(
        "alanvourch/tmdb-movies-daily-updates", path=DEST_FILE, unzip=True
    )
    print("Dataset downloaded and extracted.")


def save_csv(df: pd.DataFrame, path: str) -> None:
    """Save the cleaned CSV file to the data directory."""
    delete_if_file_exists(path)
    df.to_csv(path, index=False)
    print(f"Cleaned data saved to {path}.")


if __name__ == "__main__":
    get_kaggle_csv()
