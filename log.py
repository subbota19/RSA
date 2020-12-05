import logging


class Logging:
    def __init__(self, name):
        self.name = name
        self.log_format = f"%(asctime)s - [%(levelname)s] - %(name)s - %(message)s"

    def get_file_handler(self):
        mode = 'a'
        if self.name == '__main__':
            mode = 'w'
        file_handler = logging.FileHandler("rsa.log", mode=mode)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(logging.Formatter(self.log_format))
        return file_handler

    def get_stream_handler(self):
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        stream_handler.setFormatter(logging.Formatter(self.log_format))
        return stream_handler

    def get_logger(self):
        logger = logging.getLogger(self.name)
        logger.setLevel(logging.INFO)
        logger.addHandler(self.get_file_handler())
        return logger
