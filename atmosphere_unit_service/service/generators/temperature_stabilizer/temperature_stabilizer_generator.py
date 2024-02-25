from dataclasses import dataclass
import random

import uuid

from service.domain.temperature_stabilizer.temperature_stabilizer import TemperatureStabilizer
from service.generators.generation_strategy import IGenerationStrategy

class DefaultGenerationStrategy(IGenerationStrategy):
    @dataclass
    class GenerationParams:
        TEMPERATURE = 24.0

        SIGMA = 2.0

    def __init__(
        self,
        model: TemperatureStabilizer,
        name: str = f"TemperatureStabilizerDefaultGenerator-{uuid.uuid4()}",
    ) -> None:
        super().__init__()

        self.__model = model
        self.__name = name
    
    def generate_properties(self) -> None:
        if self.__model.is_on:
            TemperatureStabilizer.temperature = random.gauss(
                self.GenerationParams.TEMPERATURE,
                self.GenerationParams.SIGMA
            )
        else:
            pass

        self.__model.alarm = False

        if self.__model.durability <= 50:
            self.__model.alarm = True

    def name(self) -> str:
        return self.__name
    
    __model: TemperatureStabilizer = None
    __name: str = ""
    