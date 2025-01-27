import logging, os.path

formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s:  %(message)s")

class Logger:
    def __init__(self, name: str):
        assert(type(name) is str)

        self.handler = handler = logging.FileHandler(
            filename=f'{name}.log',
            mode='w'
        )

        self.handler.setFormatter(formatter)

        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(handler)

    def assertion(self, value: bool, message: str):
        if not value:
            self.logger.error(msg=message)

    def error(self, message: str):
        self.logger.error(msg=message)

    def warning(self, message: str):
        self.logger.warning(msg=message)

    def debug(self, message: str):
        self.logger.debug(msg=message)