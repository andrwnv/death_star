class HumidityManagement:

    def __init__(self, name: str = "humidity_management") -> None:
        self.name = name

        self.is_on = False
        self.alarm = False
        self.durability = 100.0

        self.sector = ""
        self.humidity = 60.0
        self.time = 0.0

    is_on: bool
    alarm: bool
    durability: float

    sector: str
    humidity: float
    time: float
    