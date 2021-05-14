from peewee import DateTimeField, AutoField, Model, SqliteDatabase
from datetime import datetime
import os

def get_database():
    if 'ADREG_TEST_DB' in os.environ:
        return SqliteDatabase(os.getenv('ADREG_TEST_DB'))

    return SqliteDatabase('adreg.db')


class BaseModel(Model):
    created_at = DateTimeField(default=datetime.now())
    updated_at = DateTimeField(default=datetime.now())
    id = AutoField(unique=True, primary_key=True)

    class Meta:
        database = get_database()
