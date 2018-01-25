import ib_insync

from logger import logger
from constants import IB_UNIVERSE
from utils import _to_utc

from data.data_class import Data


class InteractiveBrokers(Data):
    """InteractiveBrokers provides the interface to fetch live data from IB through unofficial API."""

    def __init__(self):
        Data.__init__(self)
        self.source = 'ib'
        self.api = self.connect_data_api()
        self.contracts = self.get_valid_contracts()

    def connect_data_api(self):
        """Start IB instance and connect to Trader Workstation.
        Make sure TWS is running on port 7497."""

        api = ib_insync.IB()
        api.connect('127.0.0.1', 7497, clientId=1)
        return api

    def fetch_data(self):
        """fetch_data implements the method to fetch live feed through API, including
        1. current price
        2. current order book

        Fetched data are saved into database automatically and returned in jsonified form."""

        data_dict = {
            # 'price': self.get_current_price(),
            # 'order_book': self.get_order_book(),
            # 'trades': self.get_trades(),
        }

        return self.save_data(data_dict)

    def get_valid_contracts(self):
        contracts = []
        for sec_type, symbol in IB_UNIVERSE:
            logger.info('Getting contract information: {}'.format(symbol))

            if sec_type == 'future':
                cds = self.api.reqContractDetails(Future(symbol))
                cds = sorted(cds, key=lambda x: x.realExpirationDate)
                contract = Future(symbol, cds[0].realExpirationDate, cds[1].exchange)

            contracts += [contract]
        return contracts

    def get_current_price(self):
        prices = []
        for contract in self.contracts:
            logger.info('Fetching current price: {}'.format(contract.localSymbol))
            data = self.api.reqMktData(contract, '', False, False)

            # prices += [{
            #     'ticker': ticker,
            #     'utc_time': _to_utc(data['volume']['timestamp'] / 1000),
            #     'last': float(data['last']),
            #     'bid': float(data['bid']),
            #     'ask': float(data['ask']),
            #     'volume': float(data['volume']['USD']),
            #     'source': self.source,
            # }]

        return prices
