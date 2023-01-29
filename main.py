import logging

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from endpoints.api_v1 import energy_system
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

app.include_router(energy_system.router)

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

    uvicorn.run(app, host="0.0.0.0", port=2023)
