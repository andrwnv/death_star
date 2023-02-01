from models.energy_system import CoolingSystem, VacuumVessel, MagnetSystem, PlasmaHeater
from models import LiquidStorage


class PowerCell:
    def __init__(self, name: str = 'power_cell'):
        self.name = name

        self.is_on = False
        self.alarm = False
        self.durability = 100.0

        self.cooling_system = CoolingSystem()
        self.magnet_system = MagnetSystem()
        self.plasma_heater = PlasmaHeater()
        self.vacuum_vessel = VacuumVessel()
        self.fuel_storage = LiquidStorage()

    is_on: bool
    alarm: bool

    durability: float

    cooling_system: CoolingSystem
    magnet_system: MagnetSystem
    plasma_heater: PlasmaHeater
    vacuum_vessel: VacuumVessel
    fuel_storage: LiquidStorage
