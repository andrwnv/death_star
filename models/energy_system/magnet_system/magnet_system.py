from typing import List

import inductor


class MagnetSystem:
    is_on: bool
    alarm: bool

    induction: float
    temperature: float

    output_current: float
    voltage: float

    toroidal_inductors: List[inductor.Inductor]
    poloidal_inductors: List[inductor.Inductor]
