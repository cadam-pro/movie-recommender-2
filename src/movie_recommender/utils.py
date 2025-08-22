import os
import pandas as pd


def read_csv(filepath: str) -> pd.DataFrame:
    """Read a CSV file and return its contents."""

    return pd.read_csv(filepath)


def delete_if_file_exists(filepath: str) -> None:
    """Delete if file exists at the given filepath."""
    if os.path.exists(filepath):
        os.remove(filepath)
        print(f"Deleted existing file: {filepath}")
    else:
        print(f"No file found at: {filepath}")
