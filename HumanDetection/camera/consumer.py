#import numpy as np
import cv2
import kombu
from kombu.mixins import ConsumerMixin
import os
import math
import requests
from dotenv import load_dotenv

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
        
    def get_sec(self, time_str):
        """Get Seconds from time."""
        h, m, s = time_str.split(':')
        return int(h) * 3600 + int(m) * 60 + int(s)

    # TODO function to handle video requests
    def on_message(self, body, message):
        camera_id = message.headers["camera_id"]
        timestamp_intrusion_ = message.headers["timestamp_intrusion"]
        timestamp_intrusion = self.get_sec(timestamp_intrusion_)
        
        print(f"Received frame from camera {camera_id} with timestamp {message.headers['timestamp_intrusion']}")    
        message.ack()

        #source video
        video = "./samples/people-detection.mp4" 
        
        cap = cv2.VideoCapture(video)
        frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        fps = cap.get(cv2.CAP_PROP_FPS)
        clip_duration = math.trunc(frames / fps)
        
        before_after = 10
        
        start = timestamp_intrusion - before_after
        end = timestamp_intrusion + before_after
        
        print(f"Timestamp intrusion: {timestamp_intrusion}")
        #to not overclip the video
        if start < 0:
            start = 0
        if end > clip_duration:
            end = clip_duration

        print("start: ", start)
        print("end: ", end)
            
        parts = [(start, end)]
        ret, frame = cap.read()
        h, w, _ = frame.shape
        fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        client_id = "000"
        #writers = [cv2.VideoWriter(f"./samples/intrusion-{client_id}-{camera_id}-{timestamp_intrusion}.mp4", fourcc, 10.0, (w, h)) for start, end in parts]
        writers = [cv2.VideoWriter(f"./samples/intrusion_{camera_id}_{timestamp_intrusion}.mp4", fourcc, 10.0, (w, h)) for start, end in parts]
        #writers = [cv2.VideoWriter(f"./samples/download-video.mp4", fourcc, 10.0, (w, h)) for start, end in parts]

        f = 0
        while ret:
            f += 1
            for i, part in enumerate(parts):
                start, end = part
                if start*10 <= f <= end*10:
                    writers[i].write(frame)
            ret, frame = cap.read()

        for writer in writers:
            writer.release()
        cap.release()
        
        #*send the video through the HTTP to the API
        try:
            with open(f"./samples/intrusion_{camera_id}_{timestamp_intrusion}.mp4", 'rb') as f:
                response = requests.post(os.getenv('INTRUSION_MANAGEMENT_API_URL') +'/cameras/store-video', files={'file': f})
                print(f"Clipped video sent to intrusion-management-api with status code {response.status_code}")    
        except Exception as e:
            print("Error: ", e)

        return message
        
class Consumer_video_request:

    def __init__(self, output_dir):
        self.database = {}
        self.output_dir = output_dir

    def start_processing(self, broker_url, broker_username,
                         broker_password, exchange_name, queue_name):

        # Create Connection String
        connection_string = f"amqp://{broker_username}:{broker_password}" \
            f"@{broker_url}/"

        print("Connecting to RabbitMQ...")

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
            ssl=True
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

    load_dotenv()

    # AMQP Variables
    RABBIT_MQ_URL = os.getenv('RABBIT_MQ_URL')
    RABBIT_MQ_USERNAME = os.getenv('RABBIT_MQ_USERNAME')
    RABBIT_MQ_PASSWORD = os.getenv('RABBIT_MQ_PASSWORD')
    RABBIT_MQ_EXCHANGE_NAME = os.getenv('RABBIT_MQ_EXCHANGE_NAME')
    RABBIT_MQ_QUEUE_NAME = os.getenv('RABBIT_MQ_QUEUE_NAME')
    
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