class HumidityManager:

    def __init__(self, name: str = "humidity_manager") -> None:
        self.name = name

        self.is_on = False
        self.alarm = False
        self.durability = 100.0

        self.sector = ""
        self.humidity = 60.0
        self.time = 0.0
        self.speed = 5.0

    def start(self) -> None:
        self.is_on = True

    is_on: bool
    alarm: bool
    durability: float

    sector: str
    humidity: float
    time: float
    speed: float
    