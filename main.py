from src.movie_recommender.registry import save_csv
from src.movie_recommender.params import (
    full_path_all,
    full_path_clean,
    full_path_trained,
)
from src.movie_recommender.data import read_csv, sort_df, convert_types, clean_data
from src.movie_recommender.train import train_model, find_closest_movies

if __name__ == "__main__":
    df = read_csv(full_path_all)
    df_sorted = sort_df(df)
    print(df_sorted.head())
    df_converted = convert_types(df_sorted)
    print(df_converted.dtypes)
    df_cleaned = clean_data(df_converted)
    print(df_cleaned.shape)
    save_csv(df_cleaned, full_path_clean)
    model = train_model(df_cleaned)
    save_csv(model, full_path_trained)
    recommendations = find_closest_movies(model, 424)
    print(recommendations)
