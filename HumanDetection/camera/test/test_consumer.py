import datetime
from unittest.mock import Mock
import os
import sys
import pika
import json
import kombu

sys.path.append("../")
import consumer

from unittest.mock import patch
import pika

import kombu
from kombu import Exchange, Producer



    
def test_1():
    mock = Mock()
    kombu_connection = mock
    kombu_channel = kombu_connection.channel()

    message = kombu.Message(json.dumps({"camera_id": 1, "timestamp_intrusion": "11:34:56"}), headers={"camera_id": 1, "timestamp_intrusion": "11:34:56"}, channel=kombu_channel)

    cameras_worker = consumer.Cameras_worker(mock, mock, mock, mock)
    received = cameras_worker.on_message(message.body, message)

    assert message == received
    


    




