from typing import List

from models.energy_system.battery.capacitor import Capacitor

from utils.json_serializable import IJsonSerializable


class Battery(IJsonSerializable):
    def __init__(self, name: str = 'battery') -> None:
        self.name = name

        self.is_on = False
        self.alarm = False
        self.durability = 100.0
        self.charge_level = 100.0

        self.capacitors = []
        for i in range(65):
            self.capacitors.append(Capacitor())

    def start(self) -> None:
        self.is_on = True

        for capacitor in self.capacitors:
            capacitor.start()

    is_on: bool
    alarm: bool

    durability: float
    charge_level: float

    capacitors: List[Capacitor]
