from fastapi import Depends, Response, HTTPException, status, APIRouter, UploadFile, File
import src.schemas as schemas
from fastapi.responses import ORJSONResponse
import boto3
from botocore.exceptions import NoCredentialsError
import os
import kombu
from kombu import Exchange, Producer
import json
import shutil


router = APIRouter(
    prefix="/cameras",
    tags=['Cameras']
)

#! connection to broker
kombu_connection = os.environ['AMQP_URL'] + ":5672"
kombu_exchange = "myuser"
kombu_channel = "mypassword"
kombu_producer = "request-video-exchange"
kombu_queue = "request-video-queue"


@router.get("/receive-intrusion-frame", response_model=schemas.Frame)
def receive_intrusion_frame(frame: schemas.Frame):
    attach_to_message_broker(kombu_connection, kombu_exchange, kombu_channel, kombu_producer, kombu_queue, frame)    
    return frame

def attach_to_message_broker(broker_url, broker_username,
                                 broker_password, exchange_name, queue_name, frame):
        # Create Connection String
        connection_string = f"amqp://{broker_username}:{broker_password}" \
            f"@{broker_url}/"

        # Kombu Connection
        kombu_connection = kombu.Connection(
            connection_string,
            #ssl=True
        )
        kombu_channel = kombu_connection.channel()

        # Kombu Exchange
        kombu_exchange = Exchange(
            name=exchange_name,
            type="direct",
            delivery_mode=1
        )

        # Kombu Producer
        kombu_producer = Producer(
            exchange=kombu_exchange,
            channel=kombu_channel
        )

        # Kombu Queue
        kombu_queue = kombu.Queue(
            name=queue_name,
            exchange=kombu_exchange
        )
        kombu_queue.maybe_bind(kombu_connection)
        kombu_queue.declare()
        
        kombu_producer.publish(
            body=json.dumps({"camera_id": frame.camera_id, "timestamp_intrusion": "frame.timestamp_intrusion"}),
            content_type="application/json",
            headers={
                "camera_id": frame.camera_id
            }
        )                
        #print(f"Request made to camera {frame.camera_id} with timestamp {frame.timestamp_intrusion}")

#fazer este pedido ao broker
@router.get("/request-video", status_code=status.HTTP_200_OK)
def request_video_to_cameras(frame):
    return {"frame": frame}

@router.post("/receive-video", status_code=status.HTTP_200_OK)
def receive_video_from_cameras(file: UploadFile):
    with open(file.filename, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"message": "Video received", "filename": file.filename}

@router.post("/upload-s3", status_code=status.HTTP_201_CREATED)
def save_video_to_s3():
    
    client = boto3.client(
    's3',
    aws_access_key_id = os.getenv('aws_access_key_id'),
    aws_secret_access_key = os.getenv('aws_secret_access_key'),
    region_name = os.getenv('region_name')
    )
    
    print("Uploading file to S3")
    try:
        client.upload_file("video-clips-archive", "video", "./src/routers/download-video.mp4")
        print("Download Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False
    
    
@router.get("/download-video", status_code=status.HTTP_200_OK)
def download_video_from_s3():
    client = boto3.client(
    's3',
    aws_access_key_id = os.getenv('aws_access_key_id'),
    aws_secret_access_key = os.getenv('aws_secret_access_key'),
    region_name = os.getenv('region_name')
    )
    
    try:
        client.download_file("video-clips-archive", "video", "./src/routers/download-video.mp4")
        print("Download Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False