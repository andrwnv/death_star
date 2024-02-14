from service.domain.pressure_stabilization.pressure_stabilization import PressureStabilization
from service.domain.temperature_stabilization.temperature_stabilization import TemperatureStabilization

class Device:

    def __init__(self, name: str = "device") -> None:
        self.name = name

        self.is_on = False
        self.alarm = False
        self.durability = 100.0

        self.sector = ""
        PressureStabilization.is_on = False
        TemperatureStabilization.is_on = False

    is_on: bool
    alarm: bool
    durability: float

    sector: str
