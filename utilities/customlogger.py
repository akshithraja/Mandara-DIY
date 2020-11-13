import logging
import inspect


def custom_logger():
    loggername = inspect.stack()[1][3]
    logger = logging.getLogger(__name__)
    fileHandler = logging.FileHandler("logfile.log", 'w', encoding="UTF-8")
    formatter = logging.Formatter("%(asctime)s: %(levelname)s %(name)s: %(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    logger.setLevel(logging.DEBUG)
    return logger
