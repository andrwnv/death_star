from service.domain.pressure_stabilizer.pressure_stabilizer import PressureStabilizer
from service.domain.temperature_stabilizer.temperature_stabilizer import TemperatureStabilizer
from service.domain.humidity_manager.humidity_manager import HumidityManager

class Device:

    def __init__(self, name: str = "device") -> None:
        self.name = name

        self.is_on = False
        self.alarm = False
        self.durability = 100.0

        self.sector = ""
        PressureStabilizer.is_on = False
        TemperatureStabilizer.is_on = False
        HumidityManager.is_on = False

    is_on: bool
    alarm: bool
    durability: float

    sector: str
