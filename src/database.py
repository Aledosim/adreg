from peewee import SqliteDatabase
import os

if 'ADREG_TEST_DB' in os.environ:
    database = SqliteDatabase(os.getenv('ADREG_TEST_DB'))
else:
    database = SqliteDatabase('adreg.db')
