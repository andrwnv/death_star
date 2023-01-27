import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from endpoints.api_v1 import energy_system

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
    uvicorn.run(app, host="0.0.0.0", port=2023)
