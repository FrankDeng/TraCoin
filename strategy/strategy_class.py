from abc import ABCMeta, abstractmethod

from logger import logger


class Strategy(object):
    """Strategy provides an abstract base class for trading strategies.
    Each strategy must implement specific get_data method and generate_positions method.
    Input for a specific strategy include a dict of hyper-parameters,
    and output for a strategy is a (series of) target position(s),
    in form of ticker-percentage pairs."""

    __metaclass__ = ABCMeta

    @abstractmethod
    def get_data(self):
        raise NotImplementedError("Must implement get_data() method!")

    @abstractmethod
    def generate_positions(self):
        raise NotImplementedError("Must implement generate_positions() method!")
