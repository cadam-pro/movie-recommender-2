import builtins
from registry import get_kaggle_csv, save_cleaned_csv
import pandas as pd


class DummyApi:
    def authenticate(self):
        pass

    def dataset_download_files(self, *a, **k):
        pass


def test_get_kaggle_csv(monkeypatch):
    monkeypatch.setattr("registry.delete_if_file_exists", lambda _: None)
    monkeypatch.setattr("registry.KaggleApi", lambda: DummyApi())
    monkeypatch.setattr(builtins, "print", lambda _: None)
    get_kaggle_csv()  # doit s'exécuter sans erreur


def test_save_cleaned_csv(monkeypatch, tmp_path):
    path = tmp_path / "out.csv"
    monkeypatch.setattr("registry.full_path_clean", str(path))
    monkeypatch.setattr("registry.delete_if_file_exists", lambda _: None)
    monkeypatch.setattr(builtins, "print", lambda _: None)

    df = pd.DataFrame({"a": [1, 2]})
    save_cleaned_csv(df)

    out = pd.read_csv(path)
    assert out.equals(df)
