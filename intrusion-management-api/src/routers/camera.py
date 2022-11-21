from fastapi import Depends, Response, HTTPException, status, APIRouter, UploadFile, File
import src.models.schemas as schemas
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
from botocore.exceptions import NoCredentialsError
import src.service.camera_service as camera_service
import src.service.alarm_service as alarm_service
import src.service.notification_service as notification_service

router = APIRouter(
    prefix="/intrusion-management-api/cameras",
    tags=['Cameras']
)

load_dotenv(os.path.join(os.getcwd(), "src/.env"))

kombu_connection = os.getenv('RABBIT_MQ_URL')
kombu_exchange = os.getenv('RABBIT_MQ_USERNAME')
kombu_channel = os.getenv('RABBIT_MQ_PASSWORD')
kombu_producer_camera = os.getenv('RABBIT_MQ_EXCHANGE_NAME')
kombu_producer_alarm = os.getenv('RABBIT_MQ_EXCHANGE_NAME_ALARM')
kombu_queue_camera = os.getenv('RABBIT_MQ_QUEUE_NAME')
kombu_queue_alarm = os.getenv('RABBIT_MQ_QUEUE_NAME_ALARM')

aws_access_key_id = os.getenv('aws_access_key_id')
aws_secret_access_key = os.getenv('aws_secret_access_key')
region_name = os.getenv('region_name')
bucket_name = os.getenv('bucket_name')

@router.get("/receive-intrusion-frame", response_model=schemas.Frame)
def receive_intrusion_frame(frame: schemas.Frame):
    send_message_camera = camera_service.send_message_to_broker(kombu_connection, kombu_exchange, kombu_channel, kombu_producer_camera, kombu_queue_camera, frame)
    send_message_alarm = alarm_service.send_message_to_broker(kombu_connection, kombu_exchange, kombu_channel, kombu_producer_alarm, kombu_queue_alarm, frame.camera_id)
    
    trigger_notification = notification_service.trigger_notification(frame.camera_id)
    
    if (send_message_camera and send_message_alarm) and trigger_notification:
        return Response(status_code=status.HTTP_200_OK, content="Message sent to message broker and notification triggered")
    else:
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content="Message not sent to message broker or notification not triggered")

@router.post("/store-video", status_code=status.HTTP_200_OK)
def receive_video_from_cameras_and_save(file: UploadFile):
    if not file.filename.endswith(".mp4"):
        return Response(status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE , content="File must be mp4")    
    
    try:
        with open(file.filename, 'wb') as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content="Error saving video")

    res = camera_service.save_on_s3_bucket(aws_access_key_id, aws_secret_access_key, region_name, bucket_name, file.filename, file)
    if res == FileNotFoundError:
            return Response(status_code=status.HTTP_404_NOT_FOUND, content="The file was not found")
    elif res == NoCredentialsError:
        return Response(status_code=status.HTTP_401_UNAUTHORIZED, content="Credentials not available")
    
@router.get("/intrusions-videos", status_code=status.HTTP_200_OK)
def download_video_from_s3_and_send():
    #fazer parte de ir buscar o ficheiro ao s3 do cliente
    filename = "download-video.mp4"
    
    res = camera_service.get_from_s3_bucket(aws_access_key_id, aws_secret_access_key, region_name, bucket_name, filename)
    
    if res == FileNotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND, content="The file was not found")
    elif res == NoCredentialsError:
        return Response(status_code=status.HTTP_401_UNAUTHORIZED, content="Credentials not available")
    
    try:
        return FileResponse("./videos/" + filename, media_type="video/mp4")
    except FileNotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND, content="File not found")

"""
@router.get("/intrusions-videos", status_code=status.HTTP_200_OK)
def send_intrusion_video():
    try:
        return FileResponse("./videos/download-video.mp4", media_type="video/mp4")
    except FileNotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND, content="File not found")
"""