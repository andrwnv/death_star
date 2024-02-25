from dataclasses import dataclass
from typing import List
import random

import uuid

from service.domain.pressure_stabilizer.pressure_stabilizer import PressureStabilizer
from service.generators.generation_strategy import IGenerationStrategy

class DefaultGenerationStrategy(IGenerationStrategy):
    @dataclass
    class GenerationParams:
        PRESSURE = 750
        CO2_VOLUME = 1.5
        O2_VOLUME = 20
        N2_VOLUME = 78
        OTHER_VOLUME = 0.5

        SIGMA = 2.0
    
    def __init__(
        self,
        model: PressureStabilizer,
        name: str = f"PressureStabilizerDefaultGenerator-{uuid.uuid4()}",
    ) -> None:
        super().__init__()

        self.__model = model
        self.__name = name
    
    def generate_properties(self) -> None:
        if self.__model.is_on:
            self.__model.pressure = random.gauss(
                self.GenerationParams.PRESSURE,
                self.GenerationParams.SIGMA
            )
            self.__model.CO2_volume = random.gauss(
                self.GenerationParams.CO2_VOLUME,
                self.GenerationParams.SIGMA
            )
            self.__model.O2_volume = random.gauss(
                self.GenerationParams.O2_VOLUME,
                self.GenerationParams.SIGMA
            )
            self.__model.N2_volume = random.gauss(
                self.GenerationParams.N2_VOLUME,
                self.GenerationParams.SIGMA
            )
            self.__model.other_volume = 100-sum(
                self.__model.CO2_volume,
                self.__model.O2_volume,
                self.__model.N2_volume
            )
        else:
            pass
        
        if self.__model.CO2_volume <= 3.0:
            self.__model.is_suitable = True
        
        self.__model.alarm = False

        if self.__model.durability <= 20:
            self.__model.alarm = True
    def name(self) -> str:
        return self.__name

    __model: PressureStabilizer = None
    __name: str = ""
