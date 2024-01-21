from abc import abstractmethod
from typing import Any

import pika
import json


class Publisher:
    @abstractmethod
    def publish() -> bool:
        raise NotImplementedError


class RmqPublisher(Publisher):
    def __init__(self, rmq_addr: str) -> None:
        super().__init__()

        self._queue_name = 'death-star-events'

        credentials = pika.PlainCredentials(
            username="admin",
            password="pass"
        )

        params = pika.ConnectionParameters(host=rmq_addr, port=5672, credentials=credentials)
        self._connection = pika.BlockingConnection(parameters=params)

        self._channel = self._connection.channel()

        self._channel.exchange_declare(
            exchange=self._queue_name,
            exchange_type='fanout'
        )

    def __del__(self):
        if self._connection is not None:
            self._connection.close()

    def publish(self, msg: any) -> bool:
        self._channel.basic_publish(
            exchange=self._queue_name,
            routing_key='',
            body=json.dumps(msg)
        )
