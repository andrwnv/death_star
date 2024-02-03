import asyncio

from service.api.grpc.server import GrpcServer
from service.config import Config
from service.domain.model import Model


async def run(config: Config):
    async def timer():
        import datetime

        loop = asyncio.get_running_loop()
        end_time = loop.time() + 5.0
        while True:
            print(f"1: {datetime.datetime.now()}")
            await asyncio.sleep(1)

    async def timer2():
        import datetime

        loop = asyncio.get_running_loop()
        end_time = loop.time() + 5.0
        while True:
            print(f"2: {datetime.datetime.now()}")
            await asyncio.sleep(2)

    model = Model()

    grpc_server = GrpcServer(model=model)

    await asyncio.gather(
        timer(),
        timer2(),
        grpc_server.run(
            addr=f"{config.self_props.grpc_addr}:{config.self_props.grpc_port}"
        ),
    )
