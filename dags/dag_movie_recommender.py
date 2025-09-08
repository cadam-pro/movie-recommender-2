from airflow import DAG
from airflow.decorators import task

with DAG(dag_id="daily_movie_recommender", schedule=None) as dag:

    @task
    def get_csv():
        from registry import get_kaggle_csv

        get_kaggle_csv()

    get_csv = get_csv()

    @task
    def clean_data():
        from registry import save_csv
        from data import read_csv, sort_df, convert_types, clean_data
        from params import full_path_all, full_path_clean

        df = read_csv(full_path_all)
        df_sorted = sort_df(df)
        df_converted = convert_types(df_sorted)
        df_cleaned = clean_data(df_converted)
        save_csv(df_cleaned, full_path_clean)

    clean_data = clean_data()

    @task
    def train_model():
        from registry import save_csv
        from data import read_csv
        from params import full_path_clean, full_path_trained
        from train import train_model

        df_cleaned = read_csv(full_path_clean)
        model_df, umap_model = train_model(df_cleaned)
        save_csv(model_df, full_path_trained)

    train_model = train_model()

    get_csv >> clean_data >> train_model
