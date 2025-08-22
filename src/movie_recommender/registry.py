from kaggle.api.kaggle_api_extended import KaggleApi
from params import DEST_FILE, full_path_all, full_path_clean
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


def save_cleaned_csv(df: pd.DataFrame) -> None:
    """Save the cleaned CSV file to the data directory."""
    delete_if_file_exists(full_path_clean)
    df.to_csv(full_path_clean, index=False)
    print(f"Cleaned data saved to {full_path_clean}.")


if __name__ == "__main__":
    get_kaggle_csv()
