__version__ = "1.3.1-kc1"


class MQTTException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
