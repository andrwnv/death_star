import logging
import os

import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from usecases.generators import cooling_generator

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


if __name__ == "__main__":
    import multiprocessing.pool

    from utils.event_executor import EventExecutor

    from endpoints.api_v1 import EnergySystemApiRouter
    from endpoints.api_v1 import RepairTeamApiRouter
    from models import Model

    from usecases.api import EnergySystemApiManager
    from usecases.api import RepairTeamApiManager
    from usecases.game_loop import GameLoop

    thread_pool = multiprocessing.pool.ThreadPool(processes=4)

    executor = EventExecutor(interval=0.1)
    game_loop = GameLoop(interval=0.2, event_executor=executor)

    game_loop.start(async_executor=thread_pool)

    root_router = APIRouter(prefix='/api/v1')

    model = Model()
    model.start()

    test_gen_strategy = cooling_generator.DefaultGenerationStrategy(model=model.power_cells['alpha_cell'].cooling_system)
    test_generator = cooling_generator.CoolingGenerator()
    test_generator.start(interval=1.0, start_strategy=test_gen_strategy)

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
