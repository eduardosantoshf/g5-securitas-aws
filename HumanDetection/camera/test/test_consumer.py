import datetime
from unittest.mock import Mock
import os
import sys
import pika
import json
import kombu

sys.path.append("../")
import consumer
import camera

from unittest.mock import patch
import pika

import kombu
from kombu import Exchange, Producer


def test_camera():
    #mock = Mock()
    camera_instance = camera.Camera(1, 2)
    # AMQP Variables
    RABBIT_MQ_USERNAME = "myuser"
    RABBIT_MQ_PASSWORD = "mypassword"
    RABBIT_MQ_URL = "localhost:5671"
    RABBIT_MQ_EXCHANGE_NAME = "human-detection-exchange"
    RABBIT_MQ_QUEUE_NAME = "human-detection-queue"
    #INTRUSION_MANAGEMENT_API_URL = mock
    camera_instance.attach_to_message_broker = Mock()
    camera_instance.transmit_video = Mock()




    
def test_1():
    mock = Mock()
    kombu_connection = mock
    kombu_channel = kombu_connection.channel()

    message = kombu.Message(json.dumps({"camera_id": 1, "timestamp_intrusion": "11:34:56"}), headers={"camera_id": 1, "timestamp_intrusion": "11:34:56"}, channel=kombu_channel)

    cameras_worker = consumer.Cameras_worker(mock, mock, mock, mock)
    received = cameras_worker.on_message(message.body, message)

    assert message == received
    



# AMQP Variables
#kombu_connection = "localhost:5672"
#kombu_exchange = "myuser"
#kombu_channel = "mypassword"
#kombu_producer = "request-video-exchange"
#kombu_queue = "request-video-queue"
#
## OUTPUT
#OUTPUT_DIR = "intruders"

#def test_rabbitmq():
#
#    
#
#    mock = Mock()
#    #mock_publish()
#
#    #url = f"amqp://myuser:mypassword" \
#    #        f"@localhost:5672/"
#
#    #params = pika.URLParameters(url)
#
#    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672))
#    channel = connection.channel()
#
#    channel.exchange_declare(exchange='request-video-exchange', exchange_type='fanout')
#
#    channel.basic_publish(exchange='request-video-exchange', routing_key='', body=json.dumps({"camera_id": 1, "timestamp_intrusion": "10:10:10"}))
#    print(" [x] Sent test message")
#    connection.close()
#
#    camera_consumer = consumer.Consumer_video_request(OUTPUT_DIR)
#    
#    print("aqui")
#    camera_consumer.start_processing(
#        broker_url=kombu_connection,
#        broker_username=kombu_exchange,
#        broker_password=kombu_channel,
#        exchange_name=kombu_producer,
#        queue_name=kombu_queue
#        )
#
#    #camera_consumer.start_processing(mock, mock, mock, mock, mock)
#
#    print("published")
    
    




