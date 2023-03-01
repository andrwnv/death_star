from copy import copy

from typing import Any, Dict, Optional, List, Tuple
from models.energy_system.power_cell import PowerCell
from models.location import Location

from models.repair_team.team import RepairTeam


class RepairTeamApiManager:
    def __init__(self, teams: Dict[str, RepairTeam], power_cells: Dict[str, PowerCell], async_executor) -> None:
        self.__repair_teams = teams
        self.__power_cells = power_cells
        self.__async_executor = async_executor

    def team_list(self) -> Dict[str, RepairTeam]:
        return copy(self.__repair_teams)

    def team_info(self, team_name: str) -> Optional[RepairTeam]:
        if team_name not in self.__repair_teams:
            return None
        return copy(self.__repair_teams[team_name])

    def send_team(self, team_name: str, cell_name: str, location: str) -> Tuple[bool, str]:
        if team_name not in self.__repair_teams:
            return False, f"Team with name {team_name} not found!"
        elif cell_name not in self.__power_cells:
            return False, f"Cell with name {cell_name} not found!"

        location_item = self.__get_location(cell_name, location)
        if not location_item:
            return False, f"Location not found in {cell_name}!"

        # self.__async_executor(self.__repair, team_name, location_item)

        return True, None

    def back_team(self, team_name: str) -> bool:
        if team_name not in self.__repair_teams:
            return False

        self.__repair_teams[team_name].is_busy = False
        self.__repair_teams[team_name].current_location = Location.HOME

        return True

    def __repair(team_name: str, location: Any) -> None:
        pass

    def __get_location(self, cell_name: str, location: str) -> Any | None:
        # todo(andrwnv): make it recirsive..... like IJsonSerializable

        cell = self.__power_cells[cell_name]

        # CoolingSystem
        cooling_system = cell.cooling_system
        # CoolingSystem - Turbine
        for turbine in cooling_system.turbines:
            if turbine.name == location:
                return turbine
        # CoolingSystem - LiquidCooler - LiquidStorage
        if cooling_system.liquid_cooler.liquid_storage.name == location:
            return cooling_system.liquid_cooler.liquid_storage
        # CoolingSystem - LiquidCooler - Turbine
        for turbine in cooling_system.liquid_cooler.turbines:
            if turbine.name == location:
                return turbine

        # # MagnetSystem
        magnet_system = cell.magnet_system
        # MagnetSystem - Inductor(toroidal)
        for inductor in magnet_system.toroidal_inductors:
            if inductor.name == location:
                return inductor
        # MagnetSystem - Inductor(poloidal)
        for inductor in magnet_system.poloidal_inductors:
            if inductor.name == location:
                return inductor

        # PlasmaHeater
        if cell.plasma_heater.name == location:
            return cell.plasma_heater
        
        # VacuumVessel
        if cell.vacuum_vessel.name == location:
            return cell.vacuum_vessel

        # LiquidStorage(fuel_storage)
        if cell.fuel_storage.name == location:
            return cell.fuel_storage
        
        # Battery
        battery = cell.battery
        # Battery - Capacitor
        for capacitor in battery.capacitors:
            if capacitor.name == location:
                return capacitor

        return None

    __repair_teams: Dict[str, RepairTeam] = {}
    __power_cells: Dict[str, PowerCell] = {}
