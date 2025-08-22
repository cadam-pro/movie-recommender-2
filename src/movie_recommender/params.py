import os

DEST_FILE = "data"
FILE_NAME_ALL = "TMDB_all_movies.csv"
full_path_all = os.path.join(DEST_FILE, FILE_NAME_ALL)
FILE_NAME_CLEAN = "TMDB_clean.csv"
full_path_clean = os.path.join(DEST_FILE, FILE_NAME_CLEAN)
FILE_NAME_TRAINED = "TMDB_trained.csv"
full_path_trained = os.path.join(DEST_FILE, FILE_NAME_TRAINED)
