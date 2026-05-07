import logging
import os

def get_logger(name = __name__):

    logger = logging.getLogger(name)

    if not logger.handlers:

        logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        ) 

        file_handler = logging.FileHandler("logs/ecommerce_pipeline.log")
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

def check_file_exists(path,logger):
    if os.path.exists(path):
        logger.info(f"file exists : {path}")
        return True
    else:
        logger.error(f"file does not exists : {path}")
        return False

# logger = get_logger()

# logger.info("Logger working successfully")
# logger = get_logger()

# check_file_exists("data/raw/orders.csv", logger)

# check_file_exists("data/raw/test.csv", logger)
# print(os.getcwd())

# print(os.path.exists("data/raw/orders.csv"))