from peewee import SqliteDatabase

db_file = 'adreg.db'

def create_db():
    return SqliteDatabase(db_file)
