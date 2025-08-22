import os


def delete_if_file_exists(filepath: str) -> None:
    """Delete if file exists at the given filepath."""
    if os.path.exists(filepath):
        os.remove(filepath)
        print(f"Deleted existing file: {filepath}")
    else:
        print(f"No file found at: {filepath}")
