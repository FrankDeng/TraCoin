import sys
from argparse import ArgumentParser

from logger import logger
from mapping import MODEL_MAPPING
from utils import start_session, create_table, close_session

from models import GeminiPrice, GeminiOrderBook, GeminiTrades


def create_models(drop=False):
    session, engine = start_session()
    create_table(engine, GeminiPrice, drop=drop)
    create_table(engine, GeminiOrderBook, drop=drop)
    create_table(engine, GeminiTrades, drop=drop)
    close_session(session)


def fetch_live_data(model):
    logger.info('Fetch live data: {}'.format(model))
    obj = MODEL_MAPPING[model]()
    obj.fetch_data()


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

    data_group = parser.add_argument_group('data', 'Fetch live data')
    data_group.add_argument(
        '-l', '--live', action='store_true',
        help='Fetch live data')
    data_group.add_argument(
        '-m', '--model',
        help='Data source model')
    return parser


if __name__ == '__main__':
    parser = build_parser()
    args = parser.parse_args()

    if not (args.create or args.live):
        logger.error('Please specify arguments!')
        parser.print_help()
        sys.exit()

    # create models
    if args.create:
        create_models(drop=args.drop)

    # fetch live data
    elif args.live:
        if args.model not in MODEL_MAPPING.keys():
            logger.error('Invalid data source!')
            raise ValueError('Invalid data source!')
        fetch_live_data(args.model)
