import pytest
import src

from src.data import Data


class TestData:

    def test_init(self,mocker, tmp_path):
        mocker.patch('src.data.SqliteDatabase')

        data = Data()

        # Create database object
        src.data.SqliteDatabase.assert_called_with('adreg.db')

        # Create tables
        data.database.create_tables.assert_called_once_with(data.models)

