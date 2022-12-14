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

@router.post("/receive-intrusion-frame", response_model=schemas.Frame)
def receive_intrusion_frame(frame: schemas.Frame):
    send_message_camera = camera_service.send_message_to_broker(kombu_connection, kombu_exchange, kombu_channel, kombu_producer_camera, kombu_queue_camera, frame)
    #send_message_alarm = alarm_service.send_message_to_broker(kombu_connection, kombu_exchange, kombu_channel, kombu_producer_alarm, kombu_queue_alarm, frame.camera_id)
    
    #trigger_notification = notification_service.trigger_notification(frame.camera_id)
    
    #if (send_message_camera and send_message_alarm) and trigger_notification:
    if (send_message_camera):
        return Response(status_code=status.HTTP_200_OK, content="Message sent to message broker and notification triggered")
    else:
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content="Message not sent to message broker or notification not triggered")

@router.post("/store-video", status_code=status.HTTP_200_OK)
def receive_video_from_cameras_and_save(file: UploadFile):
    if not file.filename.endswith(".mp4"):
        return Response(status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE , content="File must be mp4")    
    
    print("11111111")
    print(os.system("ls -la"))
    try:
        with open("videos_/" + file.filename, 'wb') as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        print(e)
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content="Error saving video")

    print("2222222")
    
    res = camera_service.save_on_s3_bucket(aws_access_key_id, aws_secret_access_key, region_name, bucket_name, file.filename, file)
    if res == FileNotFoundError:
            return Response(status_code=status.HTTP_404_NOT_FOUND, content="The file was not found")
    elif res == NoCredentialsError:
        return Response(status_code=status.HTTP_401_UNAUTHORIZED, content="Credentials not available")
    
    print("3333333")
    
    """try:
        os.remove("./videos_/" + file.filename)
    except Exception as e:
        print("Error deleting video: " +  e)
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content="Error deleting video")"""
    
    
    
@router.get("/intrusions-videos", status_code=status.HTTP_200_OK)
def download_video_from_s3_and_send():
    filename = "download-video.mp4"
    
    #user_video = camera_service.get_user_videos(db, user_id=user_id)
    
    res = camera_service.get_from_s3_bucket(aws_access_key_id, aws_secret_access_key, region_name, bucket_name, filename)
    
    if res == FileNotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND, content="The file was not found")
    elif res == NoCredentialsError:
        return Response(status_code=status.HTTP_401_UNAUTHORIZED, content="Credentials not available")
    
    try:
        return FileResponse("./videos_/" + filename, media_type="video/mp4")
    except FileNotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND, content="File not found")
    #finally:
        #try:
        #    os.remove("./videos/" + filename)
        #except Exception as e:
        #    print("Error deleting video: " +  e)
        #    return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content="Error deleting video")

    try:
        # print("Video {filename} sent")
        # return FileResponse("./videos_downloaded/" + video_name, media_type="video/mp4")
        return FileResponse("./videos/" + video_name, media_type="video/mp4")
    except FileNotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND, content="File not found")
    # finally:
    #     try:
    #         os.remove("./videos_downloaded/" + video_name)
    #     except Exception as e:
    #         print("Error deleting video: " +  e)
    #         return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content="Error deleting video")

@router.get("/teste", status_code=status.HTTP_200_OK)
def test(db: Session = Depends(get_db)):
    
    #return camera_service.get_user_videos(db, user_id=5)
    return camera_service.add_user_video(db, user_id=7, video_name="download-video.mp4", video_path="/tmp/" + "download-video.mp4")