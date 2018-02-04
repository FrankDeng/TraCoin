from abc import ABCMeta, abstractmethod

from logger import logger
from utils import start_session, insert_bulk, close_session

from models import CurrentPrice, OrderBook, RecentTrades, HistoricalPrices


class Api(object):
    """Api is the abstract base class for exchange trading access objects.
    Api objects should provide interface to send trading orders through API,
    record trading executions and manage accounts."""

    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    def save_data(self, model, data):
        logger.info('Saving data into database')
        session, _ = start_session()
        insert_bulk(session, model, data)
        close_session(session)
        return data

    @abstractmethod
    def query_account(self):
        raise NotImplementedError("Must implement query_account() method!")

    @abstractmethod
    def query_order(self):
        raise NotImplementedError("Must implement query_order() method!")

    @abstractmethod
    def send_limit_order(self):
        raise NotImplementedError("Must implement send_limit_order() method!")

    @abstractmethod
    def send_market_order(self):
        raise NotImplementedError("Must implement send_market_order() method!")

    @abstractmethod
    def cancel_order(self):
        raise NotImplementedError("Must implement cancel_order() method!")
