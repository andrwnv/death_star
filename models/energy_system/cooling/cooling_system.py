from typing import List

from models.energy_system.cooling.liquid_cooler import LiquidCooler
from models.energy_system.cooling.turbine import Turbine

from utils.json_serializable import IJsonSerializable


class CoolingSystem(IJsonSerializable):
    def __init__(self, name: str = 'cooling_system') -> None:
        self.name = name

        self.is_on = False
        self.alarm = False
        self.durability = 100.0

        self.turbines = []
        for i in range(6):
            self.turbines.append(Turbine())

        self.liquid_cooler = LiquidCooler()

    def start(self) -> None:
        self.is_on = True

        for turbine in self.turbines:
            turbine.start()
        self.liquid_cooler.start()

    is_on: bool
    alarm: bool

    durability: float

    turbines: List[Turbine]
    liquid_cooler: LiquidCooler
