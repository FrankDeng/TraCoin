import requests
import json
import datetime

from logger import logger
from constants import GEMINI_UNIVERSE
from utils import _to_utc

from data.data_class import Data
from models import GeminiPrice, GeminiOrderBook, GeminiTrades


class Gemini(Data):
    """Gemini provides the interface to fetch live data from Gemini through public API."""

    def __init__(self):
        self.models = {
            'price': GeminiPrice,
            'order_book': GeminiOrderBook,
            'trades': GeminiTrades,
        }

    def fetch_data(self):
        """fetch_data implements the method to fetch live feed through API, including
        1. current price
        2. current order book

        Fetched data are saved into database automatically and returned in jsonified form."""

        data_dict = {
            'price': self.get_current_price(),
            'order_book': self.get_order_book(),
        }

        return self.save_data(data_dict)

    def get_current_price(self):
        prices = []
        for ticker in GEMINI_UNIVERSE:
            logger.info('Fetching current price: {}'.format(ticker))
            endpoint = '/v1/pubticker/{}'.format(ticker)
            data = self._connect_data_api(endpoint)

            prices += [{
                'ticker': ticker,
                'utc_time': _to_utc(data['volume']['timestamp'] / 1000),
                'last': float(data['last']),
                'bid': float(data['bid']),
                'ask': float(data['ask']),
                'volume': float(data['volume']['USD']),
            }]

        return prices

    def get_order_book(self):
        order_book = []
        for ticker in GEMINI_UNIVERSE:
            logger.info('Fetching current order book: {}'.format(ticker))
            endpoint = '/v1/book/{}'.format(ticker)
            data = self._connect_data_api(endpoint)

            asks = [{
                'side': 'asks',
                'ticker': ticker,
                'utc_time': _to_utc(float(x['timestamp'])),
                'price': float(x['price']),
                'amount': float(x['amount']),
            } for x in data['asks']]
            bids = [{
                'side': 'bids',
                'ticker': ticker,
                'utc_time': _to_utc(float(x['timestamp'])),
                'price': float(x['price']),
                'amount': float(x['amount']),
            } for x in data['bids']]
            order_book += asks + bids

        return order_book

    def get_trades(self):
        trades = []
        for ticker in GEMINI_UNIVERSE:
            logger.info('Fetching recent trades: {}'.format(ticker))
            endpoint = '/v1/trades/{}?limit_trades=500'.format(ticker)
            data = self._connect_data_api(endpoint)

            trades += [{
                'ticker': ticker,
                'utc_time': _to_utc(x['timestampms'] / 1000),
                'side': x['type'],
                'price': float(x['price']),
                'amount': float(x['amount']),
            } for x in data]

        return trades

    def _connect_data_api(self, endpoint):
        """A common method to connect to Gemini public API"""

        url = 'https://api.gemini.com' + endpoint
        res = requests.get(url)

        if res.status_code == 200:
            return json.loads(res.content)
        else:
            raise ValueError(res.content)
