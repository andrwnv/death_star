import logging
import multiprocessing

from usecases.generators.base_generator import IGenerator
from usecases.generators.base_generation_strategy import IGenerationStrategy

from utils.timer import NonBlockableTimer

logger = logging.getLogger(__name__)


class CoolingGenerator(IGenerator):
    def start(self, interval: float, executor, start_strategy: IGenerationStrategy = None) -> None:
        self.__generation_strategy = start_strategy
        self.__executor = executor

        self.__timer = NonBlockableTimer(
            interval=interval, async_executor=self.__executor, callback=self.__timer_task)
        
        self.__timer.start()
        self.__is_started = True

    def stop(self) -> None:
        self.__timer.cancel()
        self.__is_started = False

    def is_started(self) -> bool:
        return self.__is_started

    def set_generation_strategy(self, strategy: IGenerationStrategy) -> None:
        self.__timer.cancel()
        self.__generation_strategy = strategy
        self.__timer.start()

    def __timer_task(self) -> None:
        if not self.is_started:
            pass

        print('im here')
        if not self.__generation_strategy:
            logger.warning(
                f"Current strategy is NONE. This startaegy won't be executed. Generation stoped!")
            self.stop()
        else:
            try:
                self.__generation_strategy.generate_properties()
                # self.__timer_task()
            except Exception as ex:
                logger.error(
                    f"Got exception while executing strategy. Generation stoped! Exception: {ex}")

    __generation_strategy: IGenerationStrategy = None
    __is_started = False
    __timer: NonBlockableTimer = None
