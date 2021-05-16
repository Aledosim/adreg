from src.database import database
from src.models.ad import Ad
from src.dto.ad_entry import AdEntryDTO


class AdRepository:

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

    @database.connection_context()
    def find_all_ads(self):
        ads = Ad.select()

        ad_entries = [AdEntryDTO.from_model(ad) for ad in ads]

        return ad_entries

    @database.connection_context()
    def find_ads_by_client(self, report_input_dto):
        ads = Ad.select().where(Ad.client == report_input_dto.client)

        ad_entries = [AdEntryDTO.from_model(ad) for ad in ads]

        return ad_entries

    @database.connection_context()
    def find_ads_by_period(self, report_input_dto):
        ads = Ad.select().where((Ad.end >= report_input_dto.start) & (Ad.start <= report_input_dto.end))

        ad_entries = [AdEntryDTO.from_model(ad) for ad in ads]

        return ad_entries

    @database.connection_context()
    def find_ads_by_client_and_period(self, report_input_dto):
        ads = Ad.select().where(
            (Ad.end >= report_input_dto.start)
            & (Ad.start <= report_input_dto.end)
            & (Ad.client == report_input_dto.client)
        )

        ad_entries = [AdEntryDTO.from_model(ad) for ad in ads]

        return ad_entries
