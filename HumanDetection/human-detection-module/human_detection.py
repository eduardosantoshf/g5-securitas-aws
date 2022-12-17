# @Author: Rafael Direito
# @Date:   2022-10-06 11:31:00 (WEST)
# @Email:  rdireito@av.it.pt
# @Copyright: Insituto de Telecomunicações - Aveiro, Aveiro, Portugal
# @Last Modified by:   Rafael Direito
# @Last Modified time: 2022-10-07 11:42:57

import numpy as np
import cv2
import sys
import kombu
from kombu.mixins import ConsumerMixin
import datetime
import os
import redis
import requests
from datetime import timedelta

# Kombu Message Consuming Human_Detection_Worker
class Human_Detection_Worker(ConsumerMixin):

    def __init__(self, connection, queues, database, output_dir, redis_url, intrusion_management_api_url):
        self.connection = connection
        self.queues = queues
        self.database = database
        self.output_dir = output_dir
        self.redis_url = redis_url
        self.intrusion_management_api_url = intrusion_management_api_url
        self.HOGCV = cv2.HOGDescriptor()
        self.HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        try:
            self.r = redis.Redis(
                        host = redis_url,
                        port = 6379,
                        #ssl=True,
                        ssl_cert_reqs = None
                    )
            print(self.r)

            #try:
            #    print(self.r.ping())
            #    print(self.r.set('foo','bar'))
            #    self.r.get('foo')
            #except Exception as e:
            #    print('get set error: ', e)

        except Exception as e:
            print('redis err: ', e)

                


    def detect_number_of_humans(self, frame):
        bounding_box_cordinates, _ = self.HOGCV.detectMultiScale(
            frame,
            winStride=(4, 4),
            padding=(8, 8),
            scale=1.03
        )
        return len(bounding_box_cordinates)


    def get_consumers(self, Consumer, channel):
        return [
            Consumer(
                queues=self.queues,
                callbacks=[self.on_message],
                accept=['image/jpeg']
                )
            ]


    def on_message(self, body, message):
        # Get message headers' information
        msg_source = int(message.headers["source"].split('_')[1])
        frame_timestamp = message.headers["timestamp"]
        frame_count = message.headers["frame_count"]
        frame_id = message.headers["frame_id"]
        frame_seconds = message.headers["frame_seconds"]
        
        print("--------------------------------------------")
        print("--------------------------------------------")
        print(frame_seconds)
        print("--------------------------------------------")
        print("--------------------------------------------")

        # Debug
        print(f"I received the frame number {frame_count} from {msg_source}" +
              f", with the timestamp {frame_timestamp}.")
        print("I'm processing the frame...")

        ts_processing_start = datetime.datetime.now()
        # Process the Frame
        # Get the original  byte array size
        size = sys.getsizeof(body) - 33
        # Jpeg-encoded byte array into numpy array
        np_array = np.frombuffer(body, dtype=np.uint8)
        np_array = np_array.reshape((size, 1))
        # Decode jpeg-encoded numpy array
        image = cv2.imdecode(np_array, 1)
        num_humans = self.detect_number_of_humans(image)

        # Compute Processing Time
        ts_processing_end = datetime.datetime.now()
        processing_duration = ts_processing_end - ts_processing_start
        processing_duration_ms = processing_duration.total_seconds() * 1000

        print(f"Frame {frame_count} has {num_humans} human(s), and was " +
              f"processed in {processing_duration_ms} ms.")

        # Save to Database
        self.create_database_entry(
            camera_id=msg_source,
            frame_id=frame_id,
            num_humans=num_humans,
            ts=frame_timestamp
        )

        print("Saved on the database")

        # Do we need to raise an alarm?
        alarm_raised = self.alarm_if_needed(
            camera_id=msg_source,
            frame_id=frame_id,
            frame_seconds=frame_seconds
        )

        if alarm_raised:
            ts_str = frame_timestamp.replace(":", "-").replace(" ", "_")
            filename = f"intruder_camera_id_{msg_source}" \
                f"_frame_id_{frame_id}" \
                f"_frame_timestamp_{ts_str}" \
                ".jpeg"
            output_image_path = os.path.join(self.output_dir, filename)
            cv2.imwrite(output_image_path, image)
            
        print("\n")

        # Remove Message From Queue
        message.ack()

    def create_database_entry(self, camera_id, frame_id, num_humans, ts):
        if num_humans > 0:
            self.r.hset(camera_id, frame_id, ts)

    def notify_management_api(self, camera_id, frame_seconds):
        print("ENTROU AQUI")
        #timestamp = timestamp.split(".")[0]
        #ts = timestamp.split(" ")[1]
        print(camera_id)
        data = {"camera_id": camera_id, "timestamp_intrusion": frame_seconds}
        print(data)
        reply = requests.post(f"{self.intrusion_management_api_url}/cameras/receive-intrusion-frame", json=data)
        print(reply)

    def alarm_if_needed(self, camera_id, frame_id, frame_seconds):

        prev1_frame_n_humans = self.r.hget(camera_id, frame_id - 1)
        prev2_frame_n_humans = self.r.hget(camera_id, frame_id - 2)
        curr_frame_n_humans = self.r.hget(camera_id, frame_id)

        if prev1_frame_n_humans and prev2_frame_n_humans and curr_frame_n_humans:
            print(f"A Human was found in frame {frame_id} on {curr_frame_n_humans.decode('utf-8')}")
            self.notify_management_api(camera_id, frame_seconds)

            return True
            
        return False


class Human_Detection_Module:

    def __init__(self, output_dir):
        self.database = {}
        self.output_dir = output_dir
        self.__bootstrap_output_directory()

    def __bootstrap_output_directory(self):
        if os.path.isdir(self.output_dir):
            files = os.listdir(self.output_dir)
            for f in files:
                os.remove(os.path.join(self.output_dir, f))
        else:
            os.mkdir(self.output_dir)

    def start_processing(self, broker_url, broker_username,
                         broker_password, exchange_name, queue_name, redis_url, intrusion_management_api_url):

        print("Connecting to the broker...")
        print(broker_username)
        print(broker_password)
        print(broker_url)

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
            ssl=True
        )
        self.kombu_connection.connect()
        print("Successfully connected to the broker!")

        # Start Human Detection Workers
        self.human_detection_worker = Human_Detection_Worker(
            connection=self.kombu_connection,
            queues=self.kombu_queues,
            database=self.database,
            output_dir=self.output_dir,
            redis_url=redis_url,
            intrusion_management_api_url=intrusion_management_api_url 
        )
        self.human_detection_worker.run()