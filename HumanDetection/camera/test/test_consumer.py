import datetime
from unittest.mock import Mock
import os
import sys
import pika
import json

sys.path.append("../")
import consumer

from unittest.mock import patch
import pika

from pytest_rabbitmq import factories
import kombu
from kombu import Exchange, Producer
from rabbitpy import Exchange, Queue

def callback_func(channel, method, properties, body):
    print("Message consumed:", body)

@patch("pika.BlockingConnection", spec=pika.BlockingConnection)
def mock_publish(mock_conn):
    def side_effect_publish(exchange, routing_key, body):
        print(f"Message published to {routing_key}:", body)

    # reroute basic_publish call to side_effect_publish 
    mock_conn.return_value.channel.return_value.basic_publish.side_effect = side_effect_publish

    # execute publishing code
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    channel.basic_publish(exchange="request-video-queue",
                    routing_key="request-video-queue",
                    body="{ Hello World! }")
    connection.close()

    




# AMQP Variables
kombu_connection = "localhost:5672"
kombu_exchange = "myuser"
kombu_channel = "mypassword"
kombu_producer = "request-video-exchange"
kombu_queue = "request-video-queue"

# OUTPUT
OUTPUT_DIR = "intruders"

def test_rabbitmq():
    mock = Mock()
    #mock_publish()

    url = f"amqp://myuser:mypassword" \
            f"@localhost:5672/"

    params = pika.URLParameters(url)

    connection = pika.BlockingConnection(params)
    channel = connection.channel()

    channel.exchange_declare(exchange='request-video-queue', exchange_type='fanout')

    message = ' '.join(sys.argv[1:]) or "info: Hello World!"
    channel.basic_publish(exchange='request-video-queue', routing_key='', body=message)
    print(" [x] Sent %r" % message)
    connection.close()

    camera_consumer = consumer.Consumer_video_request(OUTPUT_DIR)
    

    #camera_consumer.start_processing(
    #    broker_url=kombu_connection,
    #    broker_username=kombu_exchange,
    #    broker_password=kombu_channel,
    #    exchange_name=kombu_producer,
    #    queue_name=kombu_queue
    #    )

    camera_consumer.start_processing(mock, mock, mock, mock, mock)

    print("published")
    
    




