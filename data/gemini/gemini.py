import requests
import json
import datetime

from logger import logger
from constants import GEMINI_UNIVERSE

from data.data_class import Data
from models import GeminiPrice


class Gemini(Data):
    """Gemini provides the interface to fetch live data from Gemini through public API."""

    def __init__(self):
        self.models = {
            'price': GeminiPrice,
        }

    def fetch_data(self):
        data_dict = {
            'price': self._get_current_price(),
        }

        return self.save_data(data_dict)

    def _get_current_price(self):
        prices = []
        for ticker in GEMINI_UNIVERSE:
            logger.info('Fetching current price: {}'.format(ticker))
            endpoint = '/v1/pubticker/{}'.format(ticker)
            data = self._get_data_api(endpoint)

            data['ticker'] = ticker
            data['observation_time'] = data['volume']['timestamp']
            data['volume'] = data['volume']['USD']
            prices += [data]

        return prices

    def _get_data_api(self, endpoint):
        url = 'https://api.gemini.com' + endpoint
        res = requests.get(url)

        if res.status_code == 200:
            return json.loads(res.content)
        else:
            raise ValueError(res.content)
