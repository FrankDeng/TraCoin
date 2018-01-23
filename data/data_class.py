from abc import ABCMeta, abstractmethod

from logger import logger
from utils import start_session, insert_bulk, close_session


class Data(object):
    """Data is the abstract base class for exchange source data objects.
    Data objects should provide interface to fetch data through API,
    format and flatten data, and save to database."""

    __metaclass__ = ABCMeta

    def save_data(self, data_dict):
        logger.info('Saving live feed data into database')
        session, _ = start_session()

        for data_type in data_dict.keys():
            insert_bulk(session, self.models[data_type], data_dict[data_type])

        close_session(session)
        return data_dict

    @abstractmethod
    def connect_data_api(self):
        raise NotImplementedError("Must implement connect_data_api() method!")

    @abstractmethod
    def fetch_data(self):
        raise NotImplementedError("Must implement fetch_data() method!")
