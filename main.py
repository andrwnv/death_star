from usecases.abstract_scenario import AbstractScenario, AbstractAction
import logging
import os

import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from usecases.generators import battery_generator, cooling_generator, magnet_generator, plasma_heater_generator, vacuum_vessel_generator
from usecases.generators.generator import ModelPropertiesGenerator

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Death Star ACS",
    description="Death Star ACS API",
    version="0.0.1",
    contact={
        "name": "Andrew G.",
        "url": "https://github.com/andrwnv/death_star_acs",
        "email": "glazynovand@gmail.com",
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    from datetime import datetime

    debugKeyExists = 'DEBUG' in os.environ

    return {
        'debug_mode': True if debugKeyExists and os.environ['DEBUG'] else False,
        'time': datetime.now().strftime("%d.%m.%YT%H:%M:%S")
    }


class TestAction(AbstractAction):
    def __init__(self, name: str, is_extra: bool = False, period: float = 1.0) -> None:
        super().__init__(name)
        self.__is_extra = is_extra
        self._period = period

    def __call__(self) -> bool:
        print(f"Name = {self._name}. Extra = {self.__is_extra}")
        return True

    def is_end(self) -> bool:
        print(f'{self.name()} #{self.__counter} tick')
        self.__counter += 1
        return self.__counter > 3

    def is_extra_action(self) -> bool:
        return self.__is_extra

    __is_extra: bool
    __counter = 0


class TestScenario(AbstractScenario):
    def __init__(self, period: float) -> None:
        super().__init__()
        self.__period = period

    def is_end(self) -> bool:
        return self._action_queue.qsize() == 0

    def is_win(self) -> bool | None:
        return None

    def next_action_period(self) -> float:
        return self.__period

    __period: float = 1


if __name__ == "__main__":
    import multiprocessing.pool

    from usecases.event_executor import EventExecutor

    from endpoints.api_v1 import EnergySystemApiRouter
    from endpoints.api_v1 import RepairTeamApiRouter
    from models import Model

    from usecases.api import EnergySystemApiManager
    from usecases.api import RepairTeamApiManager
    from usecases.scenarist import Scenarist

    thread_pool = multiprocessing.pool.ThreadPool(processes=6)

    event_executor = EventExecutor(
        interval=0.1, async_executor=thread_pool.apply_async)
    scenarist = Scenarist(event_executor=event_executor)

    scenatio = TestScenario(period=6)

    scenatio.push_action(TestAction(name="test1", period=5))
    scenatio.push_action(TestAction(name="test2", period=5))
    scenatio.push_action(TestAction(name="test3", is_extra=True))
    scenatio.push_action(TestAction(name="test4", is_extra=True))
    scenatio.push_action(TestAction(name="test5", period=5))
    scenatio.push_action(TestAction(name="test6", period=5))
    scenatio.push_action(TestAction(name="test7", is_extra=True))
    scenatio.push_action(TestAction(name="test8", is_extra=True))
    scenatio.push_action(TestAction(name="test9", period=5))

    scenarist.set_scenario(scenatio)
    scenarist.start(async_executor=thread_pool.apply_async)

    root_router = APIRouter(prefix='/api/v1')

    model = Model()
    model.start()

    model_generator = ModelPropertiesGenerator()

    for name, cell in model.power_cells.items():
        model_generator.push_strategy(cooling_generator.DefaultGenerationStrategy(
            model=cell.cooling_system, name=f'cooling_generator-{name}'))
        model_generator.push_strategy(vacuum_vessel_generator.DefaultGenerationStrategy(
            model=cell.vacuum_vessel, name=f'vacuum_vessel_generator-{name}'))
        model_generator.push_strategy(magnet_generator.DefaultGenerationStrategy(
            model=cell.magnet_system, name=f'magnet_generator-{name}'))
        model_generator.push_strategy(plasma_heater_generator.DefaultGenerationStrategy(
            model=cell.plasma_heater, name=f'plasma_heater_generator-{name}'))
        model_generator.push_strategy(battery_generator.DefaultGenerationStrategy(
            model=cell.battery, name=f'battery_generator-{name}'))

    model_generator.start(interval=1.0, executor=thread_pool.apply_async)

    energy_system_manager = EnergySystemApiManager(
        power_cells=model.power_cells)
    energy_system_router = EnergySystemApiRouter(
        manager=energy_system_manager, prefix="/energy")

    repair_team_manager = RepairTeamApiManager(teams=model.repair_teams)
    repair_team_router = RepairTeamApiRouter(
        manager=repair_team_manager, prefix="/repair")

    root_router.include_router(energy_system_router)
    root_router.include_router(repair_team_router)

    app.include_router(root_router)

    uvicorn.run(app, host="0.0.0.0", port=2023)
