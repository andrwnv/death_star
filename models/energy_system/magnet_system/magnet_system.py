from typing import List

from models.energy_system.magnet_system.inductor import Inductor

from utils.json_serializable import IJsonSerializable


class MagnetSystem(IJsonSerializable):
    def __init__(self, name: str = 'magnet_system') -> None:
        self.name = name

        self.is_on = False
        self.alarm = False
        self.durability = 100.0
        self.induction = 0.0
        self.temperature = 0.0
        self.output_current = 0.0
        self.voltage = 0.0

        self.toroidal_inductors = []
        for i in range(5):
            self.toroidal_inductors.append(Inductor())

        self.poloidal_inductors = []
        for i in range(7):
            self.poloidal_inductors.append(Inductor())

    is_on: bool
    alarm: bool

    durability: float

    induction: float
    temperature: float

    output_current: float
    voltage: float

    toroidal_inductors: List[Inductor]
    poloidal_inductors: List[Inductor]
