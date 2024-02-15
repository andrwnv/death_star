from service.domain.pressure_balancer.pressure_balancer import PressureBalancer

class AtmosphereUnit:

    def __init__(self, name: str = "atmosphere_unit") -> None:
        self.name = name

        self.durability = 100.0

        self.avr_pressure = 750.0
        self.avr_temperature = 24.0
        self.avr_humidity = 60.0

        PressureBalancer.is_on = False
    
    durability: float

    avr_pressure: float
    avr_temperature: float
    avr_humidity: float