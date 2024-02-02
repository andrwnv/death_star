import proto.energy_unit.energy_unit_pb2 as pb2
import proto.energy_unit.energy_unit_pb2_grpc as pb2_grpc


class UnaryService(pb2_grpc.UnaryServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GetServerResponse(self, request, context):

        # get the string from the incoming request
        message = request.message
        result = f'Hello I am up and running received "{message}" message from you'
        result = {"message": result, "received": True}

        return pb2.MessageResponse(**result)


class GrpcServer:

    def __init__(self, *args, **kwargs):
        from concurrent import futures
        import grpc

        self.__is_started = False
        self.__server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))

        pb2_grpc.add_UnaryServicer_to_server(UnaryService(), self.__server)

    async def run(self, addr: str):
        import asyncio

        self.__server.add_insecure_port(addr)
        self.__server.start()

        self.__is_started = True

        while self.__is_started:
            await asyncio.sleep(1)

    def stop(self):
        self.__is_started = False
