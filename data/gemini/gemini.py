import requests

from logger import logger
from constants import GEMINI_UNIVERSE
from utils import _to_utc

from data.data_class import Data


class Gemini(Data):
    """Gemini provides the interface to fetch live data from Gemini through public API."""

    def __init__(self):
        Data.__init__(self)
        self.source = 'gemini'

    def connect_data_api(self, endpoint):
        """A common method to use Gemini public API with certain endpoint."""

        url = 'https://api.gemini.com' + endpoint
        res = requests.get(url)

        if res.status_code == 200:
            return res.json()
        else:
            raise ValueError(res.content)

    def fetch_data(self):
        """fetch_data implements the method to fetch live feed through API, including
        1. current price
        2. current order book
        3. recent 250 rows of trades

        Fetched data are saved into database automatically and returned in jsonified form."""

        data_dict = {
            'price': self.get_current_price(),
            'order_book': self.get_order_book(),
            'trades': self.get_trades(),
        }

        return self.save_data(data_dict)

    def get_current_price(self):
        prices = []
        for ticker in GEMINI_UNIVERSE:
            logger.info('Fetching current price: {}'.format(ticker))
            endpoint = '/v1/pubticker/{}'.format(ticker)
            data = self.connect_data_api(endpoint)

            prices += [{
                'ticker': ticker,
                'utc_time': _to_utc(data['volume']['timestamp'] / 1000),
                'last': float(data['last']),
                'bid': float(data['bid']),
                'ask': float(data['ask']),
                'volume': float(data['volume']['USD']),
                'source': self.source,
            }]

        return prices

    def get_order_book(self):
        order_book = []
        for ticker in GEMINI_UNIVERSE:
            logger.info('Fetching current order book: {}'.format(ticker))
            endpoint = '/v1/book/{}'.format(ticker)
            data = self.connect_data_api(endpoint)

            asks = [{
                'side': 'asks',
                'ticker': ticker,
                'utc_time': _to_utc(float(x['timestamp'])),
                'price': float(x['price']),
                'amount': float(x['amount']),
                'source': self.source,
            } for x in data['asks']]
            bids = [{
                'side': 'bids',
                'ticker': ticker,
                'utc_time': _to_utc(float(x['timestamp'])),
                'price': float(x['price']),
                'amount': float(x['amount']),
                'source': self.source,
            } for x in data['bids']]
            order_book += asks + bids

        return order_book

    def get_trades(self):
        trades = []
        for ticker in GEMINI_UNIVERSE:
            logger.info('Fetching recent trades: {}'.format(ticker))
            endpoint = '/v1/trades/{}?limit_trades=250'.format(ticker)
            data = self.connect_data_api(endpoint)

            trades += [{
                'ticker': ticker,
                'utc_time': _to_utc(x['timestampms'] / 1000),
                'side': x['type'],
                'price': float(x['price']),
                'amount': float(x['amount']),
                'source': self.source,
            } for x in data]

        return trades
