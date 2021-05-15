from src.repositories.adrepository import AdRepository


class AdReg:
    def __init__(self):
        self.data = AdRepository()

    def create_adentry(self, ad_input_dto):
        ad_entry = self.data.get_or_create_ad(ad_input_dto)
        return ad_entry

    def create_report(self, report_input_dto):
        pass
