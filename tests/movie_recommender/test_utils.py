import os
import tempfile
import pandas as pd
from utils import delete_if_file_exists, read_csv


def test_read_csv():
    df = pd.DataFrame({"a": [1, 2]})
    path = tempfile.mktemp(suffix=".csv")
    df.to_csv(path, index=False)
    out = read_csv(path)
    assert out.equals(df)
    os.remove(path)


def test_delete_existing_file():
    f = tempfile.NamedTemporaryFile(delete=False)
    f.close()
    delete_if_file_exists(f.name)
    assert not os.path.exists(f.name)


def test_delete_non_existing_file():
    path = tempfile.mktemp()
    delete_if_file_exists(path)  # ne doit pas lever d'erreur
    assert not os.path.exists(path)
