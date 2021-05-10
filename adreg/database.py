from peewee import SqliteDatabase

def create_db(db_file='adreg.db'):
    return SqliteDatabase(db_file)
