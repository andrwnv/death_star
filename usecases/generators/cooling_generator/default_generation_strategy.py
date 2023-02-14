from typing import List
import random
import uuid

from models.energy_system.cooling.cooling_system import CoolingSystem
from models.energy_system.cooling.turbine import Turbine
from usecases.generators.base_generation_strategy import IGenerationStrategy
from usecases.generators.cooling_generator.constants import CoolingDefaultParams


class DefaultGenerationStrategy(IGenerationStrategy):
    def __init__(self, model: CoolingSystem, name: str = f'CoolingSystemDefaultGenerator-{uuid.uuid4()}') -> None:
        super().__init__()

        self.__model = model
        self.__name = name

    def generate_properties(self) -> None:
        def __turbine_params_generator(turbines: List[Turbine]):
            for turbine in turbines:
                turbine.alarm = False

                if turbine.is_on:
                    turbine.input_current = random.gauss(
                        CoolingDefaultParams.INPUT_CURRENT, CoolingDefaultParams.SIGMA)
                    turbine.input_power = random.gauss(
                        CoolingDefaultParams.INPUT_POWER, CoolingDefaultParams.SIGMA)
                    turbine.input_voltage = random.gauss(
                        CoolingDefaultParams.INPUT_VOLTAGE, CoolingDefaultParams.SIGMA)
                    turbine.rpm = random.gauss(
                        CoolingDefaultParams.RPM, CoolingDefaultParams.SIGMA)

        if not self.__model.is_on:
            pass

        self.__model.alarm = False
        __turbine_params_generator(self.__model.turbines)

        self.__model.liquid_cooler.alarm = False
        if self.__model.liquid_cooler.is_on:
            __turbine_params_generator(self.__model.liquid_cooler.turbines)
            self.__model.liquid_cooler.liquid_storage.liquid_level = random.gauss(
                CoolingDefaultParams.LIQUID_LEVEL, 1.0)

    def name(self) -> str:
        return self.__name

    __model: CoolingSystem = None
    __name: str = ""
