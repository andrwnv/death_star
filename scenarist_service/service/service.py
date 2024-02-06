import asyncio
import logging

from service.config import Config

logger = logging.getLogger(__name__)


async def run(config: Config):
    async def timer():
        while True:
            logger.debug("im alive")
            await asyncio.sleep(1)

    await asyncio.gather(
        timer(),
    )
