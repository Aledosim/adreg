from peewee import SqliteDatabase

from src.models.base import get_database
from src.models.ad import Ad
from src.dto.ad_entry import AdEntryDTO


class Data:
    models = [
        Ad,
    ]
    database = get_database()

    def __init__(self):
        self.create_tables()

    @database.connection_context()
    def create_tables(self):
        self.database.create_tables(self.models)

    @database.connection_context()
    def get_or_create_ad(self, ad_dto):
        ad, is_created = Ad.get_or_create(ad_dto)
        ad_entry = AdEntryDTO.from_model(ad)
        return ad_entry
