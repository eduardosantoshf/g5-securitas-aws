from fastapi.testclient import TestClient
from fastapi import status, UploadFile
from fastapi.responses import FileResponse
import pytest

def test_receive_intrusion_frame(client: TestClient) -> None:
    post_body = {
        "camera_id": 2,
        "timestamp_intrusion": "12:00:00"
    }

    res = client.get("/intrusion-management-api/cameras/receive-intrusion-frame", json=post_body)
    assert res.status_code == status.HTTP_200_OK
    res = res.content.decode("utf-8")
    assert res == "Message sent to message broker and notification triggered"

def test_receive_intrusion_frame_invalid_camera_id(client: TestClient) -> None:
    post_body = {
        "camera_id": "XXX",
        "timestamp_intrusion": "12:00:00"
    }

    res = client.get("/intrusion-management-api/cameras/receive-intrusion-frame", json=post_body)
    assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    
    
def test_receive_intrusion_frame_invalid_timestamp(client: TestClient) -> None:
    post_body = {
        "camera_id": 3,
        "timestamp_intrusion": "2022-12-12 12:00:00"
    }

    res = client.get("/intrusion-management-api/cameras/receive-intrusion-frame", json=post_body)
    assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    
def test_receive_clipped_video_from_camera(client: TestClient) -> None:
    res = None
    with open("./videos/people-detection.mp4", "rb") as f:
        res = client.post("/intrusion-management-api/cameras/store-video", files={'file':f})
    assert res.status_code == status.HTTP_200_OK
    
def test_receive_clipped_video_from_camera_invalid_file(client: TestClient) -> None:
    res = None
    with open("people-detection.txt", "rb") as f:
        res = client.post("/intrusion-management-api/cameras/store-video", files={'file':f})
    assert res.status_code == status.HTTP_415_UNSUPPORTED_MEDIA_TYPE

def test_download_video_from_s3(client: TestClient) -> None:
    res = client.get("/intrusion-management-api/cameras/intrusions-videos")
    assert res.status_code == status.HTTP_200_OK