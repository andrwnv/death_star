from abc import ABC, abstractmethod

from usecases.generators.base_generation_strategy import IGenerationStrategy


class IGenerator(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def start(self, interval: float, start_strategy: IGenerationStrategy = None) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass

    @abstractmethod
    def is_started(self) -> bool:
        pass

    @abstractmethod
    def set_generation_strategy(self, strategy: IGenerationStrategy) -> None:
        pass
