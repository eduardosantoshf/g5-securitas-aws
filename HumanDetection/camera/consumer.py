#import numpy as np
#import cv2
import kombu
from kombu.mixins import ConsumerMixin
import os
import requests

# Kombu Message Consuming Human_Detection_Worker
class Cameras_worker(ConsumerMixin):

    def __init__(self, connection, queues, database, output_dir):
        self.connection = connection
        self.queues = queues
        self.database = database
        self.output_dir = output_dir
        #self.HOGCV = cv2.HOGDescriptor()
        #self.HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    def get_consumers(self, Consumer, channel):
        return [
            Consumer(
                queues=self.queues,
                callbacks=[self.on_message],
                #accept=['image/jpeg']
                )
            ]


    # TODO function to handle video requests
    def on_message(self, body, message):        
        response = message.body
        print(response)
        #print(message)
        
        #camera_id = message.headers["camera_id"]
        #timestamp_intrusion = message.headers["timestamp_intrusion"]
        
        #print(f"Received frame from camera {camera_id} with timestamp {timestamp_intrusion}")
        
        #*send the video through the HTTP to the API
        """
        try:
            with open('./samples/people-detection.mp4', 'rb') as f:
                response = requests.post('http://localhost:8000/cameras/receive-video', files={'file': f})
                print(response.json())
        except Exception as e:
            print("Error: ", e)
        """
class Consumer_video_request:

    def __init__(self, output_dir):
        self.database = {}
        self.output_dir = output_dir

    def start_processing(self, broker_url, broker_username,
                         broker_password, exchange_name, queue_name):

        # Create Connection String
        connection_string = f"amqp://{broker_username}:{broker_password}" \
            f"@{broker_url}/"

        # Kombu Exchange
        self.kombu_exchange = kombu.Exchange(
            name=exchange_name,
            type="direct",
        )

        # Kombu Queues
        self.kombu_queues = [
            kombu.Queue(
                name=queue_name,
                exchange=self.kombu_exchange
            )
        ]

        # Kombu Connection
        self.kombu_connection = kombu.Connection(
            connection_string,
            heartbeat=4,
            #ssl=True
        )

        # Start Human Detection Workers
        self.cameras_worker = Cameras_worker(
            connection=self.kombu_connection,
            queues=self.kombu_queues,
            database=self.database,
            output_dir=self.output_dir
        )
        self.cameras_worker.run()


if __name__ == '__main__':

    # AMQP Variables
    RABBIT_MQ_URL = os.environ['AMQP_URL'] + ":5672"
    RABBIT_MQ_USERNAME = "myuser"
    RABBIT_MQ_PASSWORD = "mypassword"
    RABBIT_MQ_EXCHANGE_NAME = "request-video-exchange"
    RABBIT_MQ_QUEUE_NAME = "request-video-queue"

    # OUTPUT
    OUTPUT_DIR = "intruders"

    camera_consumer = Consumer_video_request(OUTPUT_DIR)

    camera_consumer.start_processing(
        broker_url=RABBIT_MQ_URL,
        broker_username=RABBIT_MQ_USERNAME,
        broker_password=RABBIT_MQ_PASSWORD,
        exchange_name=RABBIT_MQ_EXCHANGE_NAME,
        queue_name=RABBIT_MQ_QUEUE_NAME
        )

    print("End of consumer")