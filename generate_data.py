import sys
from argparse import ArgumentParser

from logger import logger
from utils import start_session, create_table, close_session

from models import GeminiPrice


def create_models(drop=False):
    session, engine = start_session()
    create_table(engine, GeminiPrice, drop=drop)
    close_session(session)


def build_parser():
    parser = ArgumentParser()

    # create models
    create_group = parser.add_argument_group('create', 'Create all models')
    create_group.add_argument(
        '--create', action='store_true',
        help='Create models')
    create_group.add_argument(
        '--drop', action='store_true',
        help='Drop existing models')

    return parser


if __name__ == '__main__':
    parser = build_parser()
    args = parser.parse_args()

    if not (args.create):
        logger.error('Please specify arguments!')
        parser.print_help()
        sys.exit()

    # create models
    if args.create:
        create_models(drop=args.drop)
