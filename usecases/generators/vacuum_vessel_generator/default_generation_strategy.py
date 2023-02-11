import random
import uuid

from models.energy_system.vacuum_vessel.vacuum_vessel import VacuumVessel
from usecases.generators.base_generation_strategy import IGenerationStrategy
from usecases.generators.vacuum_vessel_generator.constants import VacuumVesselDefaultParams


class DefaultGenerationStrategy(IGenerationStrategy):
    def __init__(self, model: VacuumVessel, name: str = f'VacuumVesselDefaultGenerator-{uuid.uuid4()}') -> None:
        super().__init__()

        self.__model = model
        self.__name = name

    def generate_properties(self) -> None:
        if not self.__model.is_on:
            pass

        self.__model.alarm = False
        self.__model.input_current = random.gauss(
            VacuumVesselDefaultParams.INPUT_CURRENT, VacuumVesselDefaultParams.SIGMA)
        self.__model.input_power = random.gauss(
            VacuumVesselDefaultParams.INPUT_POWER, VacuumVesselDefaultParams.SIGMA)
        self.__model.input_voltage = random.gauss(
            VacuumVesselDefaultParams.INPUT_VOLTAGE, VacuumVesselDefaultParams.SIGMA)
        self.__model.pressure = random.gauss(
            VacuumVesselDefaultParams.PRESSURE, VacuumVesselDefaultParams.SIGMA)

    def name(self) -> str:
        return self.__name

    __model: VacuumVessel = None
    __name: str = ""
