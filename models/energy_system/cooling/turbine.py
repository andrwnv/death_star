class Turbine:
    def __init__(self, name: str = 'turbine'):
        self.name = name

        self.is_on = False
        self.alarm = False
        self.durability = 100.0

        self.rpm = 0.0
        self.input_current = 0.0
        self.input_voltage = 0.0
        self.input_power = 0.0

    is_on: bool
    alarm: bool

    durability: float

    rpm: float

    input_current: float
    input_voltage: float
    input_power: float
