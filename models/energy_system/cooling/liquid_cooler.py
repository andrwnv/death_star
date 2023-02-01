from typing import List

from models.energy_system.cooling.turbine import Turbine
from models.liquid_storage import LiquidStorage


class LiquidCooler:
    is_on: bool
    alarm: bool

    durability: float

    liquid_storage: LiquidStorage
    turbines: List[Turbine]
