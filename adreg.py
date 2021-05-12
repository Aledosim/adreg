"""
This layer comunicates with the user
"""

import logging
log = logging.getLogger()

import datetime
log.debug('\nStarting script execution at {}'.format(datetime.datetime.now()))

import argparse
from src.validation import add_ad

def add(args):
    add_ad()

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

def main():
    argument_parser = argparse.ArgumentParser()
    subparsers = argument_parser.add_subparsers()

    create_add_subparser(subparsers)

    args = argument_parser.parse_args()
    print(args.func)
    log.debug('args: {}'.format(args))
    args.func(args)

if __name__ == '__main__':
    main()
