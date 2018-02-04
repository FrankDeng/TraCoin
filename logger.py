import os
import logging
import datetime

FILENAME = 'logs/{}.log'.format(datetime.datetime.today().strftime('%Y%m%d'))


class Logger(object):
    def __init__(self):
        if not os.path.exists('logs'):
            os.mkdir('logs')

        if not os.path.exists(FILENAME):
            open(FILENAME, 'w+').close()

        logging.basicConfig(
            format='%(asctime)s.%(msecs)03d %(name)s %(levelname)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            level=logging.DEBUG,
            filename=FILENAME,
            filemode='a'
        )
        self.logger = logging.getLogger('TRACOIN')

        # add console output
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s'))
        self.logger.addHandler(ch)

    def info(self, msg):
        self.logger.info(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

logger = Logger()
