"""
This layer comunicates with the user
"""

import logging
log = logging.getLogger()

import datetime
log.debug('\nStarting script execution at {}'.format(datetime.datetime.now()))

import argparse
import sys

from src.services.adservice import AdService

def add(args):
    ad = AdService()
    ad.add(
        name=args.name,
        client=args.client,
        start=args.start,
        end=args.end,
        investment=args.investment
    )

def create_add_subparser(subparsers):
    add_parser = subparsers.add_parser(
        'add',
        description='add description',
        help='add advertisement register',
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
        help='starting date of advertisement as DD-MM-YYYY',
    )
    add_parser.add_argument(
        '--end', '-e',
        type=str,
        required=True,
        help='ending date of advertisement as DD-MM-YYYY',
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
        description='add description',
        help='make a report filtered by client and/or days interval',
    )
    report_parser.set_defaults(func=add)

    report_parser.add_argument(
        '--start', '-s',
        type=str,
        help='start date of report',
        required=True,
    )

    report_parser.add_argument(
        '--client', '-c',
        type=str,
        help='name of the client',
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
        prog='adreg'
    )
    subparsers = argument_parser.add_subparsers()

    create_add_subparser(subparsers)
    create_report_subparser(subparsers)

    args = argument_parser.parse_args()

    # If no arguments are suplied, print the help and exit
    if len(vars(args)) == 0:
        argument_parser.print_help()
        sys.exit()

    log.debug('args: {}'.format(args))
    args.func(args)

if __name__ == '__main__':
    main()
