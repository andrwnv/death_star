from typing import Type

from fastapi import APIRouter

from usecases.api.energy_system_api_manager import EnergySystemApiManager


class EnergySystemController(APIRouter):
    def __init__(self, manager: Type[EnergySystemApiManager], *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__manager = manager

        self.add_api_route(path='/state',
                           methods=['GET'], endpoint=self.get_state)
        self.add_api_route(path='/state/{power_cell_name}',
                           methods=['GET'], endpoint=self.get_cell_state)
        self.add_api_route(path='/state/{power_cell_name}/colling_system',
                           methods=['GET'], endpoint=self.get_colling_system_state)
        self.add_api_route(path='/state/{power_cell_name}/magnet_system',
                           methods=['GET'], endpoint=self.get_magnet_system_state)
        self.add_api_route(path='/state/{power_cell_name}/plasma_heater',
                           methods=['GET'], endpoint=self.get_plasma_heater_state)
        self.add_api_route(path='/state/{power_cell_name}/vacuum_vessel',
                           methods=['GET'], endpoint=self.get_vacuum_vessel_state)
        self.add_api_route(path='/state/{power_cell_name}/fuel_storage',
                           methods=['GET'], endpoint=self.get_fuel_storage_state)

    async def get_state(self):
        return {"TEST": []}

    async def get_cell_state(self, power_cell_name: str):
        return {power_cell_name: []}

    async def get_colling_system_state(self, power_cell_name: str):
        return {power_cell_name: []}

    async def get_magnet_system_state(self, power_cell_name: str):
        return {power_cell_name: ['asd']}

    async def get_plasma_heater_state(self, power_cell_name: str):
        return {power_cell_name: []}

    async def get_vacuum_vessel_state(self, power_cell_name: str):
        return {power_cell_name: []}

    async def get_fuel_storage_state(self, power_cell_name: str):
        return {power_cell_name: []}
