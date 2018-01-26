import numpy as np
import pandas as pd

from logger import logger
from utils import start_session, insert_bulk, close_session


class DataHandler(object):
    """DataHandler handles live feed data from different sources,
    transforms jsonified data into pandas data frame and pass to strategy and traders."""

    def __init__(self):
        pass
