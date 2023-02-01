from copy import copy
from typing import Dict

from models.energy_system.power_cell import PowerCell
from models.energy_system.cooling.cooling_system import CoolingSystem
from models.energy_system.magnet_system.magnet_system import MagnetSystem
from models.energy_system.plasma_heater.plasma_heater import PlasmaHeater
from models.energy_system.vacuum_vessel.vacuum_vessel import VacuumVessel
from models.liquid_storage import LiquidStorage


class EnergySystemApiManager:
    def __init__(self, power_cells: Dict[str, PowerCell]):
        self.__power_cells = power_cells

    def get_state(self, name: str) -> PowerCell:
        return copy(self.__power_cells[name])

    def get_colling_system_state(self, name: str) -> CoolingSystem:
        return copy(self.__power_cells[name].cooling_system)

    def get_magnet_system_state(self, name: str) -> MagnetSystem:
        return copy(self.__power_cells[name].magnet_system)

    def get_plasma_heater_state(self, name: str) -> PlasmaHeater:
        return copy(self.__power_cells[name].plasma_heater)

    def get_vacuum_vessel_state(self, name: str) -> VacuumVessel:
        return copy(self.__power_cells[name].vacuum_vessel)

    def get_fuel_storage_state(self, name: str) -> LiquidStorage:
        return copy(self.__power_cells[name].fuel_storage)

    def repair_colling_system(self, name: str, team_name: str) -> None:
        pass

    def repair_magnet_system(self, name: str, team_name: str) -> None:
        pass

    def repair_plasma_heater(self, name: str, team_name: str) -> None:
        pass

    def repair_vacuum_vessel(self, name: str, team_name: str) -> None:
        pass

    def repair_fuel_storage(self, name: str, team_name: str) -> None:
        pass

    __power_cells: Dict[str, PowerCell]
