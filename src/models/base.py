from peewee import DateTimeField, AutoField, Model, SqliteDatabase
from datetime import datetime

def get_database():
    return SqliteDatabase(None)


class BaseModel(Model):
    created_at = DateTimeField(default=datetime.now())
    updated_at = DateTimeField(default=datetime.now())
    id = AutoField(unique=True, primary_key=True)

    class Meta:
        database = get_database()
