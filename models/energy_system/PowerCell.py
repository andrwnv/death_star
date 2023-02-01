from models.energy_system.cooling.cooling_system import CoolingSystem
from models.energy_system.magnet_system.magnet_system import MagnetSystem
from models.energy_system.plasma_heater.plasma_heater import PlasmaHeater
from models.energy_system.vacuum_vessel.vacuum_vessel import VacuumVessel
from models.liquid_storage import LiquidStorage


class PowerCell:
    colling_system: CoolingSystem
    magnet_system: MagnetSystem
    plasma_heater: PlasmaHeater
    vacuum_vessel: VacuumVessel
    fuel_storage: LiquidStorage
