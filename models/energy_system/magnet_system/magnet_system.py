from typing import List

from models.energy_system.magnet_system.inductor import Inductor


class MagnetSystem:
    is_on: bool
    alarm: bool

    durability: float

    induction: float
    temperature: float

    output_current: float
    voltage: float

    toroidal_inductors: List[Inductor]
    poloidal_inductors: List[Inductor]
