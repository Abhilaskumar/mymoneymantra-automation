
import logging

def get_logger():
    logger = logging.getLogger("framework")
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler("reports/logs.log")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger