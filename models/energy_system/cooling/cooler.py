from typing import List

import cryostat
import turbine


class Cooler:
    is_on: bool
    alarm: bool

    cryostat: cryostat.Cryostat
    turbines: List[turbine.Turbine]
