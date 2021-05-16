from peewee import SqliteDatabase
import os

from src.models.ad import Ad

models = [
    Ad,
]

if 'ADREG_TEST_DB' in os.environ:
    database = SqliteDatabase(os.getenv('ADREG_TEST_DB'))
else:
    database = SqliteDatabase('adreg.db')

database.bind(models)
database.create_tables(models)
