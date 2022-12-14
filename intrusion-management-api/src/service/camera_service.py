from botocore.exceptions import NoCredentialsError
from sqlalchemy.orm import Session
from kombu import Exchange, Producer
from fastapi import Response, status
import kombu
import json
import boto3

import src.models.models as models

def send_message_to_broker(broker_url, broker_username, broker_password, exchange_name, queue_name, frame):
    # Create Connection String
    connection_string = f"amqp://{broker_username}:{broker_password}" \
        f"@{broker_url}/"        
    print(f"Connecting to {connection_string}")
    try:# Kombu Connection
        kombu_connection = kombu.Connection(connection_string) #ssl=True)
        kombu_channel = kombu_connection.channel()
    except Exception as e:
        print(f"Error connecting to message broker: {e}")
        return False
    # Kombu Exchange
    kombu_exchange = Exchange(name=exchange_name, type="direct", delivery_mode=1)
    # Kombu Producer
    kombu_producer = Producer(exchange=kombu_exchange, channel=kombu_channel)
    # Kombu Queue
    kombu_queue = kombu.Queue(name=queue_name, exchange=kombu_exchange)
    kombu_queue.maybe_bind(kombu_connection)
    kombu_queue.declare()
    try:
        kombu_producer.publish(
            body=json.dumps({"camera_id": frame.camera_id, "timestamp_intrusion": frame.timestamp_intrusion.strftime("%H:%M:%S")}),
            content_type="application/json",
            headers={
                "camera_id": frame.camera_id,
                "timestamp_intrusion": frame.timestamp_intrusion.strftime("%H:%M:%S")
            }
        )                
        #print(f"Request made to camera {frame.camera_id} with timestamp {frame.timestamp_intrusion}")
        return True
    except Exception as e:
        print(f"Error sending message to message broker: {e}")
        return False
    
def get_user_videos(db: Session, user_id: int) -> list:
    return db.query(models.VideoUsers).filter(models.VideoUsers.user_id == user_id).all()
    
def add_user_video(db: Session, user_id: int, video_name: str, video_path: str):
    db_user_video = models.VideoUsers(user_id=user_id, video_name=video_name, video_path=video_path)
    db.add(db_user_video)
    db.commit()
    db.refresh(db_user_video)
    return db_user_video
    
    
def save_on_s3_bucket(access_key_id, secret_access_key, region_name, bucket_name, filename, file_path):
    client = boto3.client(
    's3',
    aws_access_key_id = access_key_id,
    aws_secret_access_key = secret_access_key,
    region_name = region_name
    )

    try:
        client.upload_file(Bucket=bucket_name, Key=filename, Filename=file_path)
        return True
    except FileNotFoundError:
        return FileNotFoundError
    except NoCredentialsError:
        return NoCredentialsError
    
def get_from_s3_bucket(access_key_id, secret_access_key, region_name, bucket_name, filename):
    client = boto3.client(
    's3',
    aws_access_key_id = access_key_id,
    aws_secret_access_key = secret_access_key,
    region_name = region_name
    )
    
    print("video name: (dentro) ", filename)
    
    try:
        client.download_file(Bucket=bucket_name, Key="download-video.mp4", Filename="download-video.mp4")
        print("get_from_s3_bucket")
        return True
    except FileNotFoundError:
        print("o caralho é que nao encontras oh filho da puta")
        return FileNotFoundError
    except NoCredentialsError:
        return NoCredentialsError