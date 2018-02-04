import numpy as np
import pandas as pd

from logger import logger
from utils import start_session, insert_bulk, close_session

from mapping import DATA_MODELS


class DataHandler(object):
    """DataHandler handles live feed data from different sources,
    transforms jsonified data into pandas data frame and pass to strategy and traders."""

    def __init__(self, src_list):
        self.src_list = src_list
        self.data_models = {
            src: DATA_MODELS[src]() for src in self.src_list}
