from src.data import Data


class AdReg:
    def __init__(self):
        self.data = Data()

    def create_adreg(self, ad_dto):
        ad_entry = self.data.get_or_create_ad(ad_dto)
        return ad_entry
