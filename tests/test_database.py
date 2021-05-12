from pathlib import Path

from pytest import fail
from .fixtures import mock_model

from src.database import create_db


class TestDatabase:

    def test_create_db_file_at_correct_place(self, tmp_path):
        db_file = tmp_path.joinpath('adreg.db')

        db = create_db(db_file)
        db.connect()

        assert db_file.exists()
        assert db_file.is_file()

    def test_create_tables(self, mock_model):
        db = create_db(':memory:')

        db.bind([mock_model])
        db.create_tables([mock_model])

        assert mock_model.table_exists()
