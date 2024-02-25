from dataclasses import dataclass
from typing import List
import random

import uuid

from service.domain.humidity_manager.humidity_manager import HumidityManager
from service.generators.generation_strategy import (
    IGenerationStrategy,
)

class DefaultGenerationStrategy(IGenerationStrategy):
    @dataclass
    class GenerationParams:
        HUMIDITY = 60.0

        SIGMA = 10.0
    
    def __init__(
        self,
        model: HumidityManager,
        name: str = f"HumidityManagerDefaultGenerator-{uuid.uuid4()}",
    ) -> None:
        super().__init__()

        self.__model = model
        self.__name = name

    def generate_properties(self) -> None:
        if self.__model.is_on:
                HumidityManager.humidity = random.gauss(
                    self.GenerationParams.HUMIDITY,
                    self.GenerationParams.SIGMA,
                )
        else:
            pass

        self.__model.alarm = False

        if self.__model.durability <= 27:
             self.__model.alarm = True

    def name(self) -> str:
        return self.__name

    __model: HumidityManager = None
    __name: str = ""
