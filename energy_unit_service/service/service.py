import asyncio

from service.generator.generator import DomainGenerator
from amqp.amqp_consumer import RmqConsumer
from service.api.grpc.server import GrpcServer
from service.config import Config
from service.domain.model import Model


async def run(config: Config):
    # async def timer():
    #     import pika
    #     import json

    #     credentials = pika.PlainCredentials(
    #         username=config.self_props.event_queue_props.username,
    #         password=config.self_props.event_queue_props.password,
    #     )

    #     connection = pika.BlockingConnection(
    #         pika.ConnectionParameters(
    #             host=config.self_props.event_queue_props.addr,
    #             port=config.self_props.event_queue_props.port,
    #             credentials=credentials,
    #         )
    #     )

    #     channel = connection.channel()

    #     message = {"id": 1, "name": "name1"}

    #     while True:
    #         channel.basic_publish(
    #             exchange="",
    #             routing_key=config.self_props.event_queue_props.queue_name,
    #             body=json.dumps(message),
    #             properties=pika.BasicProperties(
    #                 delivery_mode=2,
    #             ),
    #         )
    #         print(" [x] Sent %r" % message)
    #         await asyncio.sleep(1)

    model = Model()
    domain_generator = DomainGenerator(model=model)

    rmq_consumer = RmqConsumer()

    grpc_server = GrpcServer(model=model)

    await asyncio.gather(
        domain_generator.run(),
        grpc_server.run(
            addr=f"{config.self_props.grpc_addr}:{config.self_props.grpc_port}"
        ),
        rmq_consumer.run(
            addr=config.self_props.event_queue_props.addr,
            port=config.self_props.event_queue_props.port,
            username=config.self_props.event_queue_props.username,
            password=config.self_props.event_queue_props.password,
            queue_name=config.self_props.event_queue_props.queue_name,
        ),
    )
