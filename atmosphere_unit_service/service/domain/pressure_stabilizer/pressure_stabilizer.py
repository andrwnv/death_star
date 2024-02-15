class PressureStabilizer:

    def __init__(self, name: str = "pressure_stabilizer") -> None:
        self.name = name

        self.is_on = False
        self.alarm = False
        self.durability = 100.0

        self.sector = ""
        self.is_suitable = False
        self.time = 0.0

        self.pressure = 750.0
        self.CO2_volume = 0.02
        self.O2_volume = 20
        self.N2_volume = 78
        self.other_volume = 1.98

        self.speed = 50.0
    def start(self) -> None:
        self.is_on = True

    is_on: bool
    alarm: bool
    durability: float

    sector: str
    is_suitable: bool
    time = float

    pressure: float
    CO2_volume: float
    O2_volume: float
    N2_volume: float
    other_volume: float

    speed: float