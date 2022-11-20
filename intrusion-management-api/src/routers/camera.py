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
from dotenv import load_dotenv
from fastapi.responses import FileResponse

router = APIRouter(
    prefix="/intrusion-management-api/cameras",
    tags=['Cameras']
)

load_dotenv(os.path.join(os.getcwd(), "src/.env"))

kombu_connection = os.getenv('RABBIT_MQ_URL')
kombu_exchange = os.getenv('RABBIT_MQ_USERNAME')
kombu_channel = os.getenv('RABBIT_MQ_PASSWORD')
kombu_producer = os.getenv('RABBIT_MQ_EXCHANGE_NAME')
kombu_queue = os.getenv('RABBIT_MQ_QUEUE_NAME')

@router.get("/receive-intrusion-frame", response_model=schemas.Frame)
def receive_intrusion_frame(frame: schemas.Frame):
    print(f"Received request from camera {frame.camera_id} with timestamp {frame.timestamp_intrusion}")
    attach_to_message_broker(kombu_connection, kombu_exchange, kombu_channel, kombu_producer, kombu_queue, frame)
    return frame

def attach_to_message_broker(broker_url, broker_username, broker_password, exchange_name, queue_name, frame):
        # Create Connection String
        connection_string = f"amqp://{broker_username}:{broker_password}" \
            f"@{broker_url}/"
            
        print(f"Connecting to {connection_string}")

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
            body=json.dumps({"camera_id": frame.camera_id, "timestamp_intrusion": frame.timestamp_intrusion.strftime("%H:%M:%S")}),
            content_type="application/json",
            headers={
                "camera_id": frame.camera_id,
                "timestamp_intrusion": frame.timestamp_intrusion.strftime("%H:%M:%S")
            }
        )                
        print(f"Request made to camera {frame.camera_id} with timestamp {frame.timestamp_intrusion}")

@router.post("/store-video", status_code=status.HTTP_200_OK)
def receive_video_from_cameras(file: UploadFile):

    if not file.filename.endswith(".mp4"):
        return Response(status_code=status.HTTP_400_BAD_REQUEST, content="File must be mp4")
    
    with open(file.filename, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    print("Video " + file.filename + " received.")
    
    client = boto3.client(
    's3',
    aws_access_key_id = os.getenv('aws_access_key_id'),
    aws_secret_access_key = os.getenv('aws_secret_access_key'),
    region_name = os.getenv('region_name')
    )

    try:
        #client.upload_file(Bucket="video-clips-archive", Key="video", Filename="./people-detection.mp4")
        print("Upload Successful")
        return Response(status_code=status.HTTP_200_OK)
    except NoCredentialsError:
        print("Credentials not available")
        return Response(status_code=status.HTTP_401_UNAUTHORIZED)
    except FileNotFoundError:
        print("The file was not found")
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    
@router.get("/download-video", status_code=status.HTTP_200_OK)
def download_video_from_s3():
    client = boto3.client(
    's3',
    aws_access_key_id = os.getenv('aws_access_key_id'),
    aws_secret_access_key = os.getenv('aws_secret_access_key'),
    region_name = os.getenv('region_name')
    )
    
    try:
        #client.download_file(Bucket="video-clips-archive", Key="video", Filename="./download-video.mp4")
        print("Download Successful")
        return Response(status_code=status.HTTP_200_OK)
    except FileNotFoundError:
        print("The file was not found")
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    except NoCredentialsError:
        print("Credentials not available")
        return Response(status_code=status.HTTP_401_UNAUTHORIZED)

@router.get("/intrusions-videos")
async def send_intrusion_video():
    try:
        return FileResponse("./src/routers/download-video.mp4", media_type="video/mp4")
    except FileNotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)