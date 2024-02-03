import asyncio

from service.generator.generator import DomainGenerator
from service.api.grpc.server import GrpcServer
from service.config import Config
from service.domain.model import Model


async def run(config: Config):
    # async def timer():
    #     import datetime

    #     loop = asyncio.get_running_loop()
    #     end_time = loop.time() + 5.0
    #     while True:
    #         print(f"1: {datetime.datetime.now()}")
    #         await asyncio.sleep(1)

    model = Model()
    domain_generator = DomainGenerator(model=model)

    grpc_server = GrpcServer(model=model)

    await asyncio.gather(
        domain_generator.run(),
        grpc_server.run(
            addr=f"{config.self_props.grpc_addr}:{config.self_props.grpc_port}"
        ),
    )
