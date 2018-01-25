import sys
from argparse import ArgumentParser

from logger import logger
from mapping import MODEL_MAPPING
from utils import start_session, create_table, close_session

from models import CurrentPrice, OrderBook, RecentTrades, HistoricalPrices


def create_models(drop=False):
    session, engine = start_session()
    create_table(engine, CurrentPrice, drop=drop)
    create_table(engine, OrderBook, drop=drop)
    create_table(engine, RecentTrades, drop=drop)
    create_table(engine, HistoricalPrices, drop=drop)
    close_session(session)


def fetch_live_data(models):
    for k, model in enumerate(models):
        if model not in MODEL_MAPPING.keys():
            logger.error('Invalid data source!')
            raise ValueError('Invalid data source!')

        logger.info('Fetch live data: {} ({}/{})'.format(model, str(k+1), str(len(models))))
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
        '-m', '--model', type=str, nargs='+',
        help='Data source models')
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
        models = [args.model] if type(args.model) == str else args.model
        fetch_live_data(models)
