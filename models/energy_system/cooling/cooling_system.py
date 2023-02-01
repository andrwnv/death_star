from typing import List

from models.energy_system.cooling.liquid_cooler import LiquidCooler
from models.energy_system.cooling.turbine import Turbine


class CoolingSystem:
    is_on: bool
    alarm: bool

    durability: float

    turbines: List[Turbine]
    liquid_cooler: LiquidCooler
