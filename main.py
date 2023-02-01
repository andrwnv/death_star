import logging

import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from endpoints.api_v1 import EnergySystemController
from models import Model

from usecases.api import EnergySystemApiManager
from usecases.game_loop import GameLoop

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
    logger.info("logging from the root logger")
    return {"message": "Hello World"}


if __name__ == "__main__":
    import multiprocessing.pool

    from utils.event_executor import EventExecutor

    thread_pool = multiprocessing.pool.ThreadPool(processes=4)

    executor = EventExecutor(interval=0.1)
    game_loop = GameLoop(interval=0.2, event_executor=executor)

    game_loop.start(async_executor=thread_pool)

    root_router = APIRouter(prefix='/api/v1')

    model = Model()

    energy_system_manager = EnergySystemApiManager(power_cells=model.power_cells)
    energy_system_controller = EnergySystemController(manager=energy_system_manager, prefix="/energy")

    root_router.include_router(energy_system_controller)
    app.include_router(root_router)

    uvicorn.run(app, host="0.0.0.0", port=2023)
