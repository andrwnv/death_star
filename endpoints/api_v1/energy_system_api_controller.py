from fastapi import APIRouter, HTTPException, status

from usecases.api.energy_system_api_manager import EnergySystemApiManager


class EnergySystemController(APIRouter):
    def __init__(self, manager: EnergySystemApiManager, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__manager = manager

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

    async def get_cell_state(self, power_cell_name: str):
        try:
            result = self.__manager.get_state(name=power_cell_name)
            fields = list(result.__dict__.keys())

            if result is None:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST_BAD_REQUEST)

            status_fields = ['is_on', 'alarm', 'durability']
            default_devices = [device for device in fields if device not in ['name'] + status_fields]
            only_durability_devices = ['fuel_storage']

            return {
                result.name: {
                    'state': result.to_json(fields=status_fields),
                    'devices_state': {
                        device_name: getattr(result, device_name).to_json(fields=['is_on', 'alarm', 'durability'])
                        if device_name not in only_durability_devices
                        else getattr(result, device_name).to_json(fields=['durability'])
                        for device_name in default_devices
                    }
                }
            }
        except HTTPException as ex:
            raise HTTPException(status_code=ex.status_code)
        except Exception as ex:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=ex)

    async def get_colling_system_state(self, power_cell_name: str):
        try:
            result = self.__manager.get_colling_system_state(name=power_cell_name)
            if result is None:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST_BAD_REQUEST)

            return {
                power_cell_name: {
                    result.name: result.to_json()
                }
            }
        except HTTPException as ex:
            raise HTTPException(status_code=ex.status_code)
        except Exception as ex:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=ex)

    async def get_magnet_system_state(self, power_cell_name: str):
        try:
            result = self.__manager.get_magnet_system_state(name=power_cell_name)
            if result is None:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

            return {
                power_cell_name: {
                    result.name: result.to_json()
                }
            }
        except HTTPException as ex:
            raise HTTPException(status_code=ex.status_code)
        except Exception as ex:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=ex)

    async def get_plasma_heater_state(self, power_cell_name: str):
        try:
            result = self.__manager.get_plasma_heater_state(name=power_cell_name)
            if result is None:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

            return {
                power_cell_name: {
                    result.name: result.to_json()
                }
            }
        except HTTPException as ex:
            raise HTTPException(status_code=ex.status_code)
        except Exception as ex:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=ex)

    async def get_vacuum_vessel_state(self, power_cell_name: str):
        try:
            result = self.__manager.get_vacuum_vessel_state(name=power_cell_name)
            if result is None:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

            return {
                power_cell_name: {
                    result.name: result.to_json()
                }
            }
        except HTTPException as ex:
            raise HTTPException(status_code=ex.status_code)
        except Exception as ex:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=ex)

    async def get_fuel_storage_state(self, power_cell_name: str):
        try:
            result = self.__manager.get_fuel_storage_state(name=power_cell_name)
            if result is None:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

            return {
                power_cell_name: {
                    result.name: result.to_json()
                }
            }
        except HTTPException as ex:
            raise HTTPException(status_code=ex.status_code)
        except Exception as ex:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=ex)

    __manager: EnergySystemApiManager
