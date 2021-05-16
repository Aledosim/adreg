"""
This layer communicates with the user
"""
import argparse
import sys
import datetime
from tabulate import tabulate

from src.services.adservice import AdService
from src.outputs.add import add_description
from src.outputs.main import main_description, main_epilog
from src.outputs.report import report_description


def add(args):
    service = AdService()
    service.add(
        name=args.name,
        client=args.client,
        start=args.start,
        end=args.end,
        investment=args.investment,
    )


def format_report(report_line):
    formatted_report = {
        'Name': report_line.name,
        'Client': report_line.client,
        'Start date': report_line.start.strftime('%d/%m/%Y'),
        'End date': report_line.end.strftime('%d/%m/%Y'),
        'Total invest': report_line.total / 100,
        'Max views': report_line.max_views,
        'Max clicks': report_line.max_clicks,
        'Max shares': report_line.max_shares,
    }
    return formatted_report


def report(args):
    service = AdService()
    reports = service.report(
        client=args.client,
        start=args.start,
        end=args.end,
    )
    print_report(reports)


def print_report(reports):
    reports_formatted = map(format_report, reports)
    print(tabulate(reports_formatted, headers='keys', floatfmt='.2f'))


def create_add_subparser(subparsers):
    add_parser = subparsers.add_parser(
        'add',
        description=add_description,
        help='add advertisement entry',
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    add_parser.set_defaults(func=add)

    add_parser.add_argument(
        '--name', '-n',
        type=str,
        required=True,
        help='name of the advertisement',
    )
    add_parser.add_argument(
        '--client', '-c',
        type=str,
        required=True,
        help='client name',
    )
    add_parser.add_argument(
        '--start', '-s',
        nargs='?',
        const=datetime.date.today().strftime('%d-%m-%Y'),
        default=datetime.date.today().strftime('%d-%m-%Y'),
        type=str,
        help='starting date as DD-MM-YYYY (default: current day)',
    )
    add_parser.add_argument(
        '--end', '-e',
        type=str,
        required=True,
        help='ending date as DD-MM-YYYY',
    )
    add_parser.add_argument(
        '--investment', '-i',
        type=int,
        required=True,
        help='investment per day in cents',
    )


def create_report_subparser(subparsers):
    report_parser = subparsers.add_parser(
        'report',
        description=report_description,
        help='make a report filtered by client and/or days interval',
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    report_parser.set_defaults(func=report)

    report_parser.add_argument(
        '--client', '-c',
        type=str,
        help='name of the client',
    )
    report_parser.add_argument(
        '--start', '-s',
        type=str,
        help='start date of report',
    )
    report_parser.add_argument(
        '--end', '-e',
        type=str,
        help='end date of report. Default is the current day',
        nargs='?',
        const=datetime.date.today().strftime('%d-%m-%Y'),
        default=datetime.date.today().strftime('%d-%m-%Y'),
    )


def main():
    argument_parser = argparse.ArgumentParser(
        prog='adreg',
        description=main_description,
        epilog=main_epilog,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = argument_parser.add_subparsers()

    create_add_subparser(subparsers)
    create_report_subparser(subparsers)

    args = argument_parser.parse_args()

    # If no arguments are suplied, print the help and exit
    if len(vars(args)) == 0:
        argument_parser.print_help()
        sys.exit()

    args.func(args)


if __name__ == '__main__':
    main()
