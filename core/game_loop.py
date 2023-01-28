import datetime


class GameLoop:
    def __init__(self, debug_mode: bool = False):
        self.__debug_mode = debug_mode

    _begin_timestamp: datetime.time
    __debug_mode: bool
