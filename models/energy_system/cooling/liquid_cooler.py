from typing import List

from models.energy_system.cooling.turbine import Turbine
from models.liquid_storage import LiquidStorage

from utils.json_serializable import IJsonSerializable


class LiquidCooler(IJsonSerializable):
    def __init__(self, name: str = 'liquid_cooler'):
        self.name = name

        self.is_on = False
        self.alarm = False
        self.durability = 100.0

        self.liquid_storage = LiquidStorage()
        self.turbines = []
        for i in range(6):
            self.turbines.append(Turbine())

    is_on: bool
    alarm: bool

    durability: float

    liquid_storage: LiquidStorage
    turbines: List[Turbine]
