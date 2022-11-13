from fastapi.testclient import TestClient
from fastapi import status
import pytest

from src.models import schemas


def test_create_valid_camera(client: TestClient, test_property: schemas.Property):
    
    property_id = test_property.id
    post_body = {
        "description": "camera_1: main building"
    }

    res = client.post("/sites-man-api/cameras/", params={"property_id": property_id}, json=post_body)

    new_camera = schemas.Camera(**res.json())
    assert new_camera.description == post_body["description"]
    assert new_camera.property_id == property_id
    assert res.status_code == status.HTTP_201_CREATED


def test_create_camera_invalid_property(client: TestClient, test_property: schemas.Property):

    property_id = test_property.id + 999
    post_body = {
        "description": "test_camera"
    }

    res = client.post("/sites-man-api/cameras/", params={"property_id": property_id}, json=post_body)

    assert res.status_code == status.HTTP_404_NOT_FOUND
    assert res.json().get("detail") == f"Property with id {property_id} not found"


@pytest.mark.parametrize(
    "skip, limit, total", [
        (1, 2, 2),
        (0, 3, 3),
    ])
def test_read_cameras(client: TestClient, test_cameras: list[schemas.Camera],
                         skip: int, limit: int, total: int):

    res = client.get(f"/sites-man-api/cameras/", params={"skip": str(skip), "limit": str(limit), "total": str(total)})

    schemas.Camera(**res.json()[0])
    assert len(res.json()) == total
    assert res.status_code == status.HTTP_200_OK


def test_read_camera(client: TestClient, test_camera: schemas.Camera):
    
    res = client.get(f"/sites-man-api/cameras/{test_camera.id}")

    res_camera = schemas.Camera(**res.json())
    assert res.status_code == status.HTTP_200_OK
    assert res_camera.id == test_camera.id
    assert res_camera.description == test_camera.description
    

def test_read_camera_invalid_id(client: TestClient, test_camera: schemas.Camera):

    invalid_id = test_camera.id + 999

    res = client.get(f"/sites-man-api/properties/{invalid_id}")

    assert res.status_code == status.HTTP_404_NOT_FOUND 


def test_update_camera(client: TestClient, test_camera: schemas.Camera, test_properties: list[schemas.Property]):
    
    new_property = test_properties[-1]
    
    id = test_camera.id
    new_property_id = new_property.id
    new_description = "test_update"
 
    res = client.put(f"/sites-man-api/cameras/{id}", params={"new_property_id": str(new_property_id), "new_description": new_description})

    print(res.json())
    res_camera = schemas.Camera(**res.json())

    assert res_camera.property_id == new_property_id
    assert res_camera.description == "test_update"
    assert res.status_code == status.HTTP_200_OK


def test_update_camera_invalid_property_id(client: TestClient, test_camera: schemas.Camera, test_properties: list[schemas.User]):

    new_property = test_properties[-1]

    id = test_camera.id
    new_property_id = new_property.id + 999

    res = client.put(f"/sites-man-api/cameras/{id}", params={"new_property_id": new_property_id})

    assert res.status_code == status.HTTP_404_NOT_FOUND


def test_update_camera_no_id_no_desc(client: TestClient, test_camera: schemas.Camera):

    id = test_camera.id

    res = client.put(f"/sites-man-api/cameras/{id}", params={"new_description": "", "new_property_id": 0})

    print(res.json())
    res_camera = schemas.Camera(**res.json())
    assert res_camera.property_id == test_camera.property_id
    assert res_camera.description == test_camera.description
    assert res.status_code == status.HTTP_200_OK


def test_delete_valid_camera(client: TestClient, test_camera: schemas.Camera):
    
    id = test_camera.id
    res = client.delete(f"/sites-man-api/cameras/{id}")

    assert res.status_code == status.HTTP_204_NO_CONTENT


def test_delete_invalid_camera_id(client: TestClient, test_camera: schemas.Camera):
    
    id = test_camera.id + 999
    res = client.delete(f"/sites-man-api/cameras/{id}")

    assert res.status_code == status.HTTP_404_NOT_FOUND