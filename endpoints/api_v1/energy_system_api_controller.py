from fastapi import APIRouter, HTTPException, status

from usecases.api.energy_system_api_manager import EnergySystemApiManager


class EnergySystemController(APIRouter):
    def __init__(self, manager: EnergySystemApiManager, *args, **kwargs):
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
        try:
            result = self.__manager.get_colling_system_state(name=power_cell_name)
            if result is None:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST_BAD_REQUEST)

            return {power_cell_name: {
                result.name: {
                }
            }}
        except HTTPException as ex:
            raise HTTPException(status_code=ex.status_code)
        except Exception as ex:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=ex)

    async def get_magnet_system_state(self, power_cell_name: str):
        try:
            result = self.__manager.get_magnet_system_state(name=power_cell_name)
            if result is None:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

            return {power_cell_name: {
                result.name: {
                }
            }}
        except HTTPException as ex:
            raise HTTPException(status_code=ex.status_code)
        except Exception as ex:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=ex)

    async def get_plasma_heater_state(self, power_cell_name: str):
        try:
            result = self.__manager.get_plasma_heater_state(name=power_cell_name)
            if result is None:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

            # TODO(andrwnv): struct to dict method or operator
            return {power_cell_name: {
                result.name: {
                    'is_on': result.is_on,
                    'alarm': result.alarm,
                    'durability': result.durability,
                    'temperature': result.temperature,
                    'output_power_watt': result.output_power_watt,
                    'input_current': result.input_current,
                    'input_voltage': result.input_voltage,
                }
            }}
        except HTTPException as ex:
            raise HTTPException(status_code=ex.status_code)
        except Exception as ex:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=ex)

    async def get_vacuum_vessel_state(self, power_cell_name: str):
        try:
            result = self.__manager.get_vacuum_vessel_state(name=power_cell_name)
            if result is None:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

            # TODO(andrwnv): struct to dict method or operator
            return {power_cell_name: {
                result.name: {
                    'is_on': result.is_on,
                    'alarm': result.alarm,
                    'durability': result.durability,
                    'pressure': result.pressure,
                    'input_current': result.input_current,
                    'input_voltage': result.input_voltage,
                    'input_power': result.input_power,
                }
            }}
        except HTTPException as ex:
            raise HTTPException(status_code=ex.status_code)
        except Exception as ex:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=ex)

    async def get_fuel_storage_state(self, power_cell_name: str):
        try:
            result = self.__manager.get_fuel_storage_state(name=power_cell_name)
            if result is None:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

            # TODO(andrwnv): struct to dict method or operator
            return {power_cell_name: {
                result.name: {
                    'durability': result.durability,
                    'liquid_level': result.liquid_level
                }
            }}
        except HTTPException as ex:
            raise HTTPException(status_code=ex.status_code)
        except Exception as ex:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=ex)

    __manager: EnergySystemApiManager
