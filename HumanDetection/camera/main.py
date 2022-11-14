# @Author: Rafael Direito
# @Date:   2022-10-06 10:54:18 (WEST)
# @Email:  rdireito@av.it.pt
# @Copyright: Insituto de Telecomunicações - Aveiro, Aveiro, Portugal
# @Last Modified by:   Rafael Direito
# @Last Modified time: 2022-10-06 11:19:15

import os
from camera import Camera

# CAMERA VARIABLES
CAMERA_ID = 1
NUM_FRAMES_PER_SECOND_TO_PROCESS = 2

# AMQP Variables
RABBIT_MQ_URL = "b-1360ad08-90a3-4944-9178-2d50e2d5ba78.mq.eu-west-3.amazonaws.com:5671"
RABBIT_MQ_USERNAME = "human-detection-broker"
RABBIT_MQ_PASSWORD = "broker32745#"
RABBIT_MQ_EXCHANGE_NAME = "human-detection-exchange"
RABBIT_MQ_QUEUE_NAME = "human-detection-queue"
INTRUSION_MANAGEMENT_API_URL = "https://hllwa7dyek.execute-api.eu-west-3.amazonaws.com/v1/intrusion-management-api"

camera = Camera(
    camera_id=CAMERA_ID,
    frames_per_second_to_process=NUM_FRAMES_PER_SECOND_TO_PROCESS
    )

camera.attach_to_message_broker(
    broker_url=RABBIT_MQ_URL,
    broker_username=RABBIT_MQ_USERNAME,
    broker_password=RABBIT_MQ_PASSWORD,
    exchange_name=RABBIT_MQ_EXCHANGE_NAME,
    queue_name=RABBIT_MQ_QUEUE_NAME
    )

camera.transmit_video("samples/people-detection.mp4")

print("End of video transmission")
