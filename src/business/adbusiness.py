from src.repositories.adrepository import AdRepository
from src.dto.report import ReportDTO
from src.libs.calculator import calculator


def calculate_total(ad_entry):
    n_days = ad_entry.end - ad_entry.start

    views, clicks, shares = calculator(ad_entry.investment)

    max_views = views * n_days.days
    max_clicks = clicks * n_days.days
    max_shares = shares * n_days.days
    total = ad_entry.investment * n_days.days

    return total, max_views, max_clicks, max_shares


class AdReg:
    def __init__(self):
        self.data = AdRepository()

    def create_adentry(self, ad_input_dto):
        ad_entry = self.data.get_or_create_ad(ad_input_dto)
        return ad_entry

    def create_report(self, report_input_dto):
        all_ads = self.data.find_all_ads()

        reports = []
        for ad_entry in all_ads:
            total, max_views, max_clicks, max_shares = calculate_total(ad_entry)

            report_dto = ReportDTO.from_ad_entry(
                ad_entry,
                total=total,
                max_views=max_views,
                max_clicks=max_clicks,
                max_shares=max_shares,
            )

            reports.append(report_dto)

        return reports
