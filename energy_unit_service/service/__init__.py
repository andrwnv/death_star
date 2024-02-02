import asyncio


async def run():
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

    from service.api.grpc.server import GrpcServer
    grpc_server = GrpcServer()

    await asyncio.gather(
        timer(),
        timer2(),
        grpc_server.run(addr="0.0.0.0:4040"),
    )
