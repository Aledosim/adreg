from src.repositories.adrepository import AdRepository


class AdReg:
    def __init__(self):
        self.data = AdRepository()

    def create_adreg(self, ad_dto):
        ad_entry = self.data.get_or_create_ad(ad_dto)
        return ad_entry
