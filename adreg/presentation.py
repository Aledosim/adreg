"""
This layer comunicates with the user
"""

import logging
log = logging.getLogger()

import datetime
log.debug('\nStarting script execution at {}'.format(datetime.datetime.now()))

import argparse

def add(args):
    print(args)

argument_parser = argparse.ArgumentParser()
subparsers = argument_parser.add_subparsers()

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

if __name__ == '__main__':
    args = argument_parser.parse_args()
    log.debug('args: {}'.format(args))
    args.func(args)
