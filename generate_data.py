import sys
from argparse import ArgumentParser

from logger import logger
from mapping import DB_TABLES, DATA_MODELS
from utils import start_session, create_table, close_session


def create_models(tables, drop=False):
    session, engine = start_session()
    for table in tables:
        logger.info('Creating table: {} ({}/{})'.format(table, str(k+1), str(len(tables))))
        create_table(engine, DB_TABLES[table], drop=drop)
    close_session(session)


def fetch_live_data(models):
    for k, model in enumerate(models):
        if model not in DATA_MODELS.keys():
            logger.error('Invalid data source!')
            raise ValueError('Invalid data source!')

        logger.info('Fetch live data: {} ({}/{})'.format(model, str(k+1), str(len(models))))
        obj = DATA_MODELS[model]()
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
    create_group.add_argument(
        '-t', '--table', type=str, nargs='+',
        help='Database tables to be created')

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
        tables = [args.table] if type(args.table) == str else args.table
        create_models(drop=args.drop)

    # fetch live data
    elif args.live:
        models = [args.model] if type(args.model) == str else args.model
        fetch_live_data(models)
