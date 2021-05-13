from peewee import SqliteDatabase
from src.models.ad import Ad


class Data:
    models = [
        Ad,
    ]

    def __init__(self):
        self.database = SqliteDatabase('adreg.db')
        self.database.create_tables(self.models)
