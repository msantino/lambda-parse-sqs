import sys
import os
import logging

def config_log(level="INFO"):
    log_level = os.getenv("LOGGING_LEVEL", level)
    logger = logging.getLogger()
    for h in logger.handlers:
        logger.removeHandler(h)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s [%(funcName)s] %(message)s'))
    logger.addHandler(handler)
    logger.setLevel(log_level)
    return logger
