from fastapi import Depends, Response, status, APIRouter, UploadFile
import src.models.schemas as schemas
from botocore.exceptions import NoCredentialsError
import os
import shutil
from dotenv import load_dotenv
from fastapi.responses import FileResponse
from botocore.exceptions import NoCredentialsError
import src.service.camera_service as camera_service
import src.service.alarm_service as alarm_service
import src.service.notification_service as notification_service
from sqlalchemy.orm import Session
from src.database import get_db
import time

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

API_URL = os.getenv('SITES_MAN_API_URL')


@router.post("/receive-intrusion-frame", response_model=schemas.Frame)
def receive_intrusion_frame(frame: schemas.Frame):
    send_message_camera = camera_service.send_message_to_broker(kombu_connection, kombu_exchange, kombu_channel, kombu_producer_camera, kombu_queue_camera, frame)
    send_message_alarm = alarm_service.send_message_to_broker(kombu_connection, kombu_exchange, kombu_channel, kombu_producer_alarm, kombu_queue_alarm, frame.camera_id)
    
    trigger_notification = notification_service.trigger_notification("fernando.silva.g5securitas@gmail.com", frame.camera_id)
    
    #if (send_message_camera and send_message_alarm) and trigger_notification:
    if (send_message_camera):
        return Response(status_code=status.HTTP_200_OK, content="Message sent to message broker and notification triggered")
    else:
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content="Message not sent to message broker or notification not triggered")

@router.post("/store-video", status_code=status.HTTP_200_OK)
def receive_video_from_cameras_and_save(file: UploadFile, db: Session = Depends(get_db)):
    if not file.filename.endswith(".mp4"):
        return Response(status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE , content="File must be mp4")    
    
    try:
        with open("videos_/" + file.filename, 'wb') as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        print(e)
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content="Error saving video")
    
    camera_id = file.filename.split("_")[1]
    print(camera_id)

    user_id, building_id = camera_service.get_user_id_and_building_id(API_URL=API_URL, camera_id=camera_id)
    print(user_id, building_id)
    
    add_info = camera_service.add_user_video(db, user_id=user_id, video_name=file.filename, video_path="./videos_/" + file.filename, camera_id=camera_id, building_id=building_id)
    if add_info == False:
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content="Error saving video info")
        
    res = camera_service.save_on_s3_bucket(aws_access_key_id, aws_secret_access_key, region_name, bucket_name, file.filename, file)
    if res == FileNotFoundError:
            return Response(status_code=status.HTTP_404_NOT_FOUND, content="The file was not found")
    elif res == NoCredentialsError:
        return Response(status_code=status.HTTP_401_UNAUTHORIZED, content="Credentials not available")
    
    #try:
    #    os.remove("./videos_/" + file.filename)
    #    print("Video deleted")
    #except Exception as e:
    #    print("Error deleting video: " +  e)
    #    return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content="Error deleting video")
    
@router.get("/intrusions-videos/{id}", status_code=status.HTTP_200_OK)
def download_video_from_s3_and_send(id: int, db: Session = Depends(get_db)):
    #id = 1 #id (row de onde clica no watch video list do front end)
    #id é o id da tabela user_videos
    user_video = camera_service.get_user_videos(db, id=id)

    video_name = user_video[0].video_name
    
    print("nome do video q está na base de dados:", video_name)
    res = camera_service.get_from_s3_bucket(aws_access_key_id, aws_secret_access_key, region_name, bucket_name, video_name)
    
    if res == FileNotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND, content="The file was not found")
    elif res == NoCredentialsError:
        return Response(status_code=status.HTTP_401_UNAUTHORIZED, content="Credentials not available")
        
    try:
        return FileResponse("./videos_/" + video_name, media_type="video/mp4")
    except FileNotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND, content="File not found")
    #finally:
    #    try:
    #        os.remove("./videos_/" + video_name)
    #    except Exception as e:
    #        print("Error deleting video: " +  e)
    #        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content="Error deleting video")