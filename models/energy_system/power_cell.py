from models.energy_system import CoolingSystem, VacuumVessel, MagnetSystem, PlasmaHeater
from models import LiquidStorage
from models.energy_system.battery.battery import Battery

from utils.json_serializable import IJsonSerializable


class PowerCell(IJsonSerializable):
    def __init__(self, name: str = 'power_cell') -> None:
        self.name = name

        self.is_on = False
        self.alarm = False
        self.durability = 100.0

        self.cooling_system = CoolingSystem()
        self.magnet_system = MagnetSystem()
        self.plasma_heater = PlasmaHeater()
        self.vacuum_vessel = VacuumVessel()
        self.fuel_storage = LiquidStorage()
        self.battery = Battery()

        self.power = 0.0

    def start(self) -> None:
        self.is_on = True

        self.cooling_system.start()
        self.magnet_system.start()
        self.plasma_heater.start()
        self.vacuum_vessel.start()
        self.battery.start()
    
    name: str

    is_on: bool
    alarm: bool

    durability: float

    cooling_system: CoolingSystem
    magnet_system: MagnetSystem
    plasma_heater: PlasmaHeater
    vacuum_vessel: VacuumVessel
    fuel_storage: LiquidStorage
    battery: Battery

    power: float

