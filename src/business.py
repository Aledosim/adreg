from src.data import Data


class AdReg:
    def __init__(self):
        self.data = Data()

    def create_adreg(self, ad_dto):
        self.data.find_one(ad_dto)

        ad_entry = self.data.get_or_create_entry(ad_dto)
        return ad_entry
