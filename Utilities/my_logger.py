import logging


def initialize_logger(loglevel):
    logger = logging.getLogger(__name__)
    # logger.setLevel(loglevel)
    formater = logging.Formatter('%(levelname)s:%(name)s::%(message)s')
    fh = logging.FileHandler('Logs/test.log', mode='w')
    fh.setFormatter(formater)
    fh.setLevel(loglevel)
    logger.addHandler(fh)
    return logger