from kaggle.api.kaggle_api_extended import KaggleApi
from params import DEST_FILE, full_path_all
from utils import delete_if_file_exists


def get_kaggle_csv() -> None:
    """Download the CSV file from Kaggle."""
    delete_if_file_exists(full_path_all)
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(
        "alanvourch/tmdb-movies-daily-updates", path=DEST_FILE, unzip=True
    )
    print("Dataset downloaded and extracted.")


if __name__ == "__main__":
    get_kaggle_csv()
