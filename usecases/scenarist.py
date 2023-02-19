import abc
import datetime
import logging
from typing import Callable

from event_executor import EventExecutor
from abstract_scenario import AbstractScenario

logger = logging.getLogger(__name__)


class Scenarist:
    def __init__(self, interval: float, event_executor: EventExecutor,
                 scenario: AbstractScenario = None, debug_mode: bool = False) -> None:

        self.__interval = interval
        self.__event_executor = event_executor
        self._debug_mode = debug_mode

        if scenario:
            self.__active_scenario = scenario

    def start(self, async_executor: Callable) -> None:
        self.__is_running = True

        if not self.__active_scenario:
            logger.error("Can't run scenarist! No active scenario for run!")
            raise RuntimeError

        self.__event_executor.start()
        async_executor(self.__job)

    def stop(self) -> None:
        self.__is_running = False

    def is_running(self) -> bool:
        return self.__is_running

    def __job(self) -> None:
        from time import sleep

        try:
            while self.__is_running:
                try:
                    self.tick_handler()
                except Exception as ex:
                    logger.error(
                        f"Error while executing scenario action. Exception: {ex}")
                sleep(self.__interval)
        except Exception as ex:
            logger.error(f"Internal error. Exception: {ex}")

    __is_running: bool = False

    __active_scenario: AbstractScenario = None

    __event_executor: EventExecutor = None
    __interval: float = 0.1

    _begin_timestamp: datetime.time = None
    _debug_mode: bool = False
