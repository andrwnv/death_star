import random
import uuid

from death_star.entities.models.energy_system.plasma_heater.plasma_heater import PlasmaHeater
from death_star.generators.base_generation_strategy import IGenerationStrategy
from death_star.generators.plasma_heater_generator.constants import PlasmaHeaterDefaultParams


class DefaultGenerationStrategy(IGenerationStrategy):
    def __init__(self, model: PlasmaHeater, name: str = f'PlasmaHeaterDefaultGenerator-{uuid.uuid4()}') -> None:
        super().__init__()

        self.__model = model
        self.__name = name

    def generate_properties(self) -> None:
        if not self.__model.is_on:
            pass

        self.__model.alarm = False

        temperature = random.gauss(
            PlasmaHeaterDefaultParams.TEMPERATURE, PlasmaHeaterDefaultParams.TEMPERATURE_SIGMA)

        self.__model.temperature = temperature if temperature < PlasmaHeaterDefaultParams.TEMPERATURE else PlasmaHeaterDefaultParams.TEMPERATURE + \
            random.random() * 10 ** -4

        self.__model.output_power_watt = random.gauss(
            PlasmaHeaterDefaultParams.OUTPUT_POWER, PlasmaHeaterDefaultParams.SIGMA)
        self.__model.input_current = random.gauss(
            PlasmaHeaterDefaultParams.INPUT_CURRENT, PlasmaHeaterDefaultParams.SIGMA)
        self.__model.input_voltage = random.gauss(
            PlasmaHeaterDefaultParams.INPUT_VOLTAGE, PlasmaHeaterDefaultParams.SIGMA)
        self.__model.input_power = random.gauss(
            PlasmaHeaterDefaultParams.INPUT_POWER, PlasmaHeaterDefaultParams.SIGMA)

        if self.__model.durability <= 30:
            self.__model.alarm = True

    def name(self) -> str:
        return self.__name

    __model: PlasmaHeater = None
    __name: str = ""
