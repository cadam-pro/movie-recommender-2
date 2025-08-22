import builtins
from data import get_kaggle_csv


class DummyApi:
    def authenticate(self):
        pass

    def dataset_download_files(self, *a, **k):
        pass


def test_get_kaggle_csv(monkeypatch):
    monkeypatch.setattr("data.delete_if_file_exists", lambda _: None)
    monkeypatch.setattr("data.KaggleApi", lambda: DummyApi())
    monkeypatch.setattr(builtins, "print", lambda _: None)
    get_kaggle_csv()  # doit s'exécuter sans erreur
