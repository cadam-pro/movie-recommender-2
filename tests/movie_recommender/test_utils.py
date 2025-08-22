import os
import tempfile
from utils import delete_if_file_exists


def test_delete_existing_file():
    f = tempfile.NamedTemporaryFile(delete=False)
    f.close()
    delete_if_file_exists(f.name)
    assert not os.path.exists(f.name)


def test_delete_non_existing_file():
    path = tempfile.mktemp()
    delete_if_file_exists(path)  # ne doit pas lever d'erreur
    assert not os.path.exists(path)
