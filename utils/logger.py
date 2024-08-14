import logging
import os

def setup_logger(name, log_file, level=logging.INFO):
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

# Example of how to use the logger
if __name__ == "__main__":
    log_file = os.path.join("logs", "app.log")
    logger = setup_logger("my_app_logger", log_file)
    logger.info("This is an info message")
