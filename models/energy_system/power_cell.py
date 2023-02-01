from models.energy_system import CoolingSystem, VacuumVessel, MagnetSystem, PlasmaHeater
from models import LiquidStorage


class PowerCell:
    is_on: bool
    alarm: bool

    durability: float

    cooling_system: CoolingSystem
    magnet_system: MagnetSystem
    plasma_heater: PlasmaHeater
    vacuum_vessel: VacuumVessel
    fuel_storage: LiquidStorage
