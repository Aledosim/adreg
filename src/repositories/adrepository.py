from peewee import SqliteDatabase

from src.database import database
from src.models.ad import Ad
from src.dto.ad_entry import AdEntryDTO


class Data:

    database = database

    @database.connection_context()
    def get_or_create_ad(self, ad_dto):
        ad, is_created = Ad.get_or_create(
            name=ad_dto.name,
            client=ad_dto.client,
            start=ad_dto.start,
            end=ad_dto.end,
            investment=ad_dto.investment
        )
        ad_entry = AdEntryDTO.from_model(ad)
        return ad_entry
