import logging
from typing import Dict

from death_star.generators.base_generator import IGenerator
from death_star.generators.base_generation_strategy import IGenerationStrategy

from utils.timer import NonBlockableTimer

logger = logging.getLogger(__name__)


class ModelPropertiesGenerator(IGenerator):
    def start(self, interval: float, executor) -> None:
        self.__executor = executor

        self.__timer = NonBlockableTimer(
            interval=interval, async_executor=self.__executor, callback=self.__generation_task)

        self.__timer.start()
        self.__is_started = True

    def stop(self) -> None:
        self.__timer.stop()
        self.__is_started = False

    def is_started(self) -> bool:
        return self.__is_started

    def push_strategy(self, strategy: IGenerationStrategy) -> None:
        self.__generation_strategies[strategy.name()] = strategy

    def delete_strategy(self, strategy_name: str) -> None:
        if strategy_name in self.__generation_strategies:
            del self.__generation_strategies[strategy_name]

    def __generation_task(self) -> None:
        if not self.is_started:
            pass

        if len(self.__generation_strategies.keys()) == 0:
            logger.warning(
                f"No strategies for generations. Generations stoped!")
            self.stop()
        else:
            for name, strategy in self.__generation_strategies.items():
                try:
                    strategy.generate_properties()
                    logger.debug(f"{name} strategy was executed!")
                except Exception as ex:
                    logger.error(
                        f"Got exception while executing {name} strategy. Generation stoped! Exception: {ex}")

    __generation_strategies: Dict[str, IGenerationStrategy] = {}
    __is_started = False
    __timer: NonBlockableTimer = None
