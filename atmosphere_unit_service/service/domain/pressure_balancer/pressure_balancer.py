from typing import List

import uuid

from service.domain.device.device import Device

class PressureBalancer:
    
    def __init__(self, name: str = "pressure_balancer") -> None:
        self.name = name

        self.is_on = False
        self.alarm = False
        self.durability = 100.0

        self.devices = []
        for _ in range(15):
            self.devices.append(Device(name=f"Device-{uuid.uuid4()}"))

    def start(self) -> None:
        self.is_on = True
        for device in self.devices:
            device.start()

    is_on: bool
    alarm: bool
    durability: float

    devices: List[Device]

        