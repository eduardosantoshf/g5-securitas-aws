from fastapi import Depends, Response, HTTPException, status, APIRouter, UploadFile, File
import src.schemas as schemas
from fastapi.responses import ORJSONResponse
import boto3
from botocore.exceptions import NoCredentialsError

router = APIRouter(
    prefix="/cameras",
    tags=['Cameras']
)
@router.post("/receive-intrusion-frame", response_model=schemas.Frame)
def receive_intrusion_frame(frame: schemas.Frame):
    request_video_to_cameras(frame)
    return frame

@router.get("/request-video", status_code=status.HTTP_200_OK)
def request_video_to_cameras(frame):
    return {"frame": frame}

@router.post("/upload-s3", status_code=status.HTTP_201_CREATED)
def save_video_to_s3():
    
    client = boto3.client(
    's3',
    aws_access_key_id = 'AKIA32O63NC3DL72P3VW',
    aws_secret_access_key = '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',
    region_name = 'eu-west-1'
    )
    
    try:
        client.upload_file("./src/routers/people-detection.mp4", "video-clips-archive", "video")
        print("Upload Successful")
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
    aws_access_key_id = 'AKIA32O63NC3DL72P3VW',
    aws_secret_access_key = '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',
    region_name = 'eu-west-1'
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