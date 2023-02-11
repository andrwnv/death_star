import logging
from threading import Timer

from usecases.generators.base_generator import IGenerator
from usecases.generators.base_generation_strategy import IGenerationStrategy
from usecases.generators.cooling_generator.default_generation_strategy import DefaultGenerationStrategy

logger = logging.getLogger(__name__)


class CoolingGenerator(IGenerator):
    def start(self, interval: float, start_strategy: IGenerationStrategy = None) -> None:
        self.__generation_strategy = start_strategy

        self.__timer = Timer(interval=interval, function=self.__timer_task)

        self.__timer_task()  # force first start
        self.__timer.start()

        self.__is_started = False

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
        print('im here')
        if not self.__generation_strategy:
            logger.error(
                f"Current strategy is NONE. This startaegy won't be executed. Generation stoped!")
            self.stop()
        else:
            self.__generation_strategy.generate_properties()
            # self.__timer.start()

    __generation_strategy: IGenerationStrategy = None
    __is_started = False
    __timer: Timer = None
