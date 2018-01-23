import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from logger import logger
from settings import SQL_URI


# SQL ORM wrapper
def start_session():
    logger.info('Starting database session')
    engine = create_engine(SQL_URI, echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session, engine


def create_table(engine, model, drop=False):
    if model.__table__.exists(engine):
        if drop:
            model.__table__.drop(engine)
        else:
            logger.error('Model exists!')
            raise

    model.__table__.create(engine)
    logger.info('Model created: {}'.format(model.__tablename__))


def insert_bulk(session, model, df):
    logger.info('Inserting data into database')
    data = df if type(df) == list else df.to_dict('record')
    session.bulk_insert_mappings(model, data)
    session.commit()


def close_session(session):
    logger.info('Committing changes and closing database session')
    session.commit()
    session.close()


# convert epoch to utc datetime
def _to_utc(timestamp):
    return datetime.datetime.utcfromtimestamp(timestamp)
