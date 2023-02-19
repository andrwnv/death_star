import uuid
import logging
import multiprocessing

from typing import Callable, Dict, List

from usecases.abstract_event import AbstractEvent
from utils.timer import NonBlockableTimer

logger = logging.getLogger(__name__)


class EventExecutor:
    def __init__(self, interval: float, async_executor: Callable, debug_mode: bool = False) -> None:
        self.__debug_mode = debug_mode
        self.__interval = interval

        self.__is_running = False
        self.__active_events = {}
        self.__ready_to_execute_events = []

        self.__timer = NonBlockableTimer(self.__interval, async_executor=async_executor, callback=self.__job)

    def start(self) -> None:
        self.__timer.start()
        self.__is_running = True

    def stop(self) -> None:
        self.__timer.stop()
        self.__is_running = False

    def is_running(self) -> bool:
        return self.__is_running

    def push_event(self, event: AbstractEvent) -> None:
        if not event:
            logger.warning(f"Unsuccessful push none {event.name()} event!")
            return

        self.__active_events.append(event)

    def __job(self) -> None:
        from time import sleep

        try:
            self.__prepare_ready_events()
            if len(self.__ready_to_execute_events) > 0:
                try:
                    self.__execute_event(
                        self.__ready_to_execute_events.pop())
                except Exception as ex:
                    logger.warning(
                        f"Error while executing event. Exception: {ex}")
        except Exception as ex:
            logger.error(f"Internal error. Exception: {ex}")

    def __execute_event(self, event: AbstractEvent) -> bool:
        if not event:
            logger.warning(
                f"Unsuccessful execution of NULL {event.name()} event!")
            return False

        try:
            if not self.__debug_mode:
                event.negative_effect()
            event.positive_effect()
            return True
        except Exception as ex:
            logger.error(
                f"Error while execute {event.name()} event effects. Exception: {ex}")
            return False

    def __prepare_ready_events(self) -> None:
        for key, event in self.__active_events:
            if self.__debug_mode:
                logger.debug(
                    f"{key}: Event {event.name()} time to execution = {event.is_soon()}")

            if event.is_ready():
                self.__ready_to_execute_events.append(
                    self.__active_events.pop(key))

    __debug_mode: bool

    __is_running: bool
    __interval: float

    __active_events: Dict[uuid.UUID, AbstractEvent]
    __ready_to_execute_events: List[AbstractEvent]

    __timer: NonBlockableTimer = None
