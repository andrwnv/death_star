import abc
import datetime
import logging
from typing import Callable

from utils.event_executor import EventExecutor

logger = logging.getLogger(__name__)


class AbstractGameLoop:
    def __init__(self, interval: float, event_executor: EventExecutor, debug_mode: bool = False):
        self.__interval = interval
        self.__event_executor = event_executor
        self._debug_mode = debug_mode

    def start(self, async_executor: Callable) -> None:
        self.__is_running = True

        self.__event_executor.start()
        async_executor(self.__job)

    def stop(self) -> None:
        self.__is_running = False

    def is_running(self) -> bool:
        return self.__is_running

    def __job(self):
        from time import sleep

        try:
            while self.__is_running:
                try:
                    self.tick_handler()
                except Exception as ex:
                    logger.error(
                        f"Error while executing tick_handler. Exception: {ex}")
                sleep(self.__interval)
        except Exception as ex:
            logger.error(f"Internal error. Exception: {ex}")

    @abc.abstractmethod
    def tick_handler(self):
        raise NotImplementedError

    __is_running: bool = False

    __event_executor: EventExecutor = None
    __interval: float = 0.1

    _begin_timestamp: datetime.time = None
    _debug_mode: bool = False
