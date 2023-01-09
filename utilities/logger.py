import logging


class TestLogger:

    @staticmethod
    def get_logger() -> logging:

        logger = logging.getLogger('orange_hrm_tests')
        file_handler = logging.FileHandler('orange_hrm_tests.log')
        file_handler.setFormatter(logging.Formatter())
        logger.addHandler(file_handler)
        logger.setLevel(logging.DEBUG)

        return logger
