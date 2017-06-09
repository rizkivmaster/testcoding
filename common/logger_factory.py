import logging
import traceback
from logging.handlers import TimedRotatingFileHandler

from common.config import general_config


class Logger(object):
    def __init__(self, name=None, filename='log/bayarkan.log'):
        """
        :type name: str
        :param name:
        :return:
        """
        self.__logger = logging.getLogger(name)
        file_handler = TimedRotatingFileHandler(filename,
                                                    when="D",
                                                    interval=1,
                                                    backupCount=5)
        # create console handler and set level to debug
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - {0} - %(message)s'.format(name)))
        ch = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - {0} - %(message)s'.format(name))
        ch.setFormatter(formatter)
        self.__logger.addHandler(ch)
        self.__logger.addHandler(file_handler)
        self.__logger.setLevel(logging.DEBUG)

    def error(self, message, *args, **kwargs):
        """
        :type e :Exception
        :param e:
        :return:
        """
        self.__logger.error(message, exc_info=True, *args, **kwargs)
        traceback.print_exc()

    def info(self, message, *args, **kwargs):
        self.__logger.info(message, *args, **kwargs)

    def debug(self, message, *args, **kwargs):
        self.__logger.debug(message, *args, **kwargs)

    def warning(self, message, *args, **kwargs):
        self.__logger.warning(message, *args, **kwargs)


def create_logger(name):
    return Logger(name=name, filename=general_config.get_general_log_path()+name+'.log')
