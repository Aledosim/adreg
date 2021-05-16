from src.repositories.adrepository import AdRepository
from src.dto.report import ReportDTO
from src.libs.calculator import calculator


def calculate_total(ad_entry, delta_days):
    views, clicks, shares = calculator(ad_entry.investment)

    max_views = views * delta_days.days
    max_clicks = clicks * delta_days.days
    max_shares = shares * delta_days.days
    total = ad_entry.investment * delta_days.days

    return total, max_views, max_clicks, max_shares


def make_report_by_client(ad_entries):
    reports = []
    for ad_entry in ad_entries:
        n_days = ad_entry.end - ad_entry.start
        total, max_views, max_clicks, max_shares = calculate_total(ad_entry, n_days)

        report_dto = ReportDTO.from_ad_entry(
            ad_entry,
            total=total,
            max_views=max_views,
            max_clicks=max_clicks,
            max_shares=max_shares,
        )

        reports.append(report_dto)

    return reports


def make_report_by_period(ad_entries, report_input):
    n_days = report_input.end - report_input.start
    reports = []
    for ad_entry in ad_entries:
        total, max_views, max_clicks, max_shares = calculate_total(ad_entry, n_days)

        if ad_entry.start < report_input.start:
            ad_entry.start = report_input.start
        if ad_entry.end > report_input.end:
            ad_entry.end = report_input.end

        report_dto = ReportDTO.from_ad_entry(
            ad_entry,
            total=total,
            max_views=max_views,
            max_clicks=max_clicks,
            max_shares=max_shares,
        )

        reports.append(report_dto)

    return reports


def make_report_by_client_and_period(ad_entries, report_input):
    reports = []
    n_days = report_input.end - report_input.start
    for ad_entry in ad_entries:
        total, max_views, max_clicks, max_shares = calculate_total(ad_entry, n_days)

        ad_entry.start = report_input.start
        ad_entry.end = report_input.end

        report_dto = ReportDTO.from_ad_entry(
            ad_entry,
            total=total,
            max_views=max_views,
            max_clicks=max_clicks,
            max_shares=max_shares,
        )

        reports.append(report_dto)

    return reports


def make_generic_report(ad_entries):
    return make_report_by_client(ad_entries)


class AdReg:
    def __init__(self):
        self.data = AdRepository()

    def create_adentry(self, ad_input_dto):
        ad_entry = self.data.get_or_create_ad(ad_input_dto)
        return ad_entry

    def create_report(self, report_input_dto):


        # Filtered by client
        if report_input_dto.client is not None and report_input_dto.start is None:
            ads = self.data.find_ads_by_client(report_input_dto)
            return make_report_by_client(ads)

        # Filtered by period
        elif report_input_dto.client is None and report_input_dto.start is not None:
            ads = self.data.find_ads_by_period(report_input_dto)
            return make_report_by_period(ads, report_input_dto)

        # Filtered by client and period
        elif report_input_dto.client is not None and report_input_dto.start is not None:
            ads = self.data.find_ads_by_client_and_period(report_input_dto)
            return make_report_by_client_and_period(ads, report_input_dto)

        # Generic report
        else:
            ads = self.data.find_all_ads()
            return make_generic_report(ads)
