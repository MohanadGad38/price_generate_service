from dataclasses import dataclass
import time
import random
from typing import List
import logging
import pika
from pika.adapters.blocking_connection import BlockingChannel
import pika.connection
import json
credentials = pika.PlainCredentials('mohanad.gad', '19941994')
connection_params = pika.ConnectionParameters(
    host='localhost',
    port=5672,
    virtual_host='/',
    credentials=credentials
)
connection = pika.BlockingConnection(connection_params)
channel: BlockingChannel = connection.channel()
queue = channel.queue_declare("stock.price")
queue_name = queue.method.queue

channel.queue_bind(exchange="Stocks", queue=queue_name,
                   routing_key="stock.price")


def callback(ch, method, properties, body):
    payload = json.loads(body)
    print('email {}'.format(payload['email']))
    print("recivied")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(on_message_callback=callback, queue=queue_name)
channel.start_consuming()
