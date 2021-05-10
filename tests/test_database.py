from .context import adreg

from pytest import fail
from pathlib import Path

from adreg.database import create_db


class TestDatabase:

    def test_create_db_file_at_correct_place(self, tmp_path):
        db_file = tmp_path.joinpath('adreg.db')
        adreg.database.db_file = db_file

        db = create_db()
        db.connect()

        assert db_file.exists()
        assert db_file.is_file()
