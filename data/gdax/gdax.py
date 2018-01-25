import requests
import json
import datetime

from logger import logger
from constants import GDAX_UNIVERSE
from utils import _to_utc

from data.data_class import Data


class GDAX(Data):
    """GDAX provides the interface to fetch live data from GDAX through public API."""

    def __init__(self):
        Data.__init__(self)
        self.source = 'gdax'

    def connect_data_api(self, endpoint):
        """A common method to use Gemini public API with certain endpoint."""

        url = 'https://api.gdax.com' + endpoint
        res = requests.get(url)

        if res.status_code == 200:
            return res.json()
        else:
            raise ValueError(res.content)

    def fetch_data(self):
        """fetch_data implements the method to fetch live feed through API, including
        1. current price
        2. current order book

        Fetched data are saved into database automatically and returned in jsonified form."""

        data_dict = {
            'price': self.get_current_price(),
        }

        return self.save_data(data_dict)

    def get_current_price(self):
        prices = []
        for ticker in GDAX_UNIVERSE:
            logger.info('Fetching current price: {}'.format(ticker))
            endpoint = '/products/{}/ticker'.format(ticker)
            data = self.connect_data_api(endpoint)

            prices += [{
                'ticker': ticker.replace('-', ''),
                'utc_time': datetime.datetime.strptime(data['time'], "%Y-%m-%dT%H:%M:%S.%fZ"),
                'last': float(data['price']),
                'bid': float(data['bid']),
                'ask': float(data['ask']),
                'volume': float(data['volume']),
                'source': self.source,
            }]

        return prices

    def get_historical_candles(self, granularity='min'):
        num_granularity = {
            'min': 60,
            '5min': 300,
            '15min': 900,
            'hour': 3600,
            '6hour': 21600,
            'daily': 86400,
        }[granularity]
        historical = []

        for ticker in GDAX_UNIVERSE:
            logger.info('Fetching current price: {}'.format(ticker))
            endpoint = '/products/{}/candles?granularity={}'.format(ticker, str(num_granularity))
            data = self.connect_data_api(endpoint)

            historical += [{
                'ticker': ticker.replace('-', ''),
                'utc_time': _to_utc(x[0]),
                'open': x[1],
                'high': x[2],
                'low': x[3],
                'close': x[4],
                'volume': x[5],
                'source': self.source,
            } for x in data]

        return historical
