class TemperatureStabilization:

    def __init__(self, name: str = "temperature_stabilization") -> None:
        self.name = name

        self.is_on = False
        self.alarm = False
        self.durability = 100.0

        self.sector = ""
        self.temperature = 24.0
        self.time = 0.0
        self.speed = 50.0

    def start(self) -> None:
        self.is_on = True
    
    is_on: bool
    alarm: bool
    durability: float

    sector: str
    temperature: float
    time: float
    speed: float
