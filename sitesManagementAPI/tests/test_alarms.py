from fastapi.testclient import TestClient
from fastapi import status

import pytest

from src.models import schemas
from tests.conf_idp import setup_test_idp


def test_create_valid_alarm(client: TestClient, test_property: schemas.Property):
    
    property_id = test_property.id
    post_body = {
        "description": "alarm_1: main building"
    }

    res = client.post("/sites-man-api/alarms/", params={"property_id": property_id}, json=post_body)

    new_alarm = schemas.Alarm(**res.json())
    assert new_alarm.description == post_body["description"]
    assert new_alarm.property_id == property_id
    assert res.status_code == status.HTTP_201_CREATED


def test_create_alarm_invalid_property(client: TestClient, test_property: schemas.Property):

    property_id = test_property.id + 999
    post_body = {
        "description": "test_alarm"
    }

    res = client.post("/sites-man-api/alarms/", params={"property_id": property_id}, json=post_body)

    assert res.status_code == status.HTTP_404_NOT_FOUND
    assert res.json().get("detail") == f"Property with id {property_id} not found"


@pytest.mark.parametrize(
    "skip, limit, total", [
        (1, 2, 2),
        (0, 3, 3),
    ])
def test_read_alarms(client: TestClient, test_alarms: list[schemas.Alarm],
                         skip: int, limit: int, total: int):

    res = client.get(f"/sites-man-api/alarms/", params={"skip": str(skip), "limit": str(limit), "total": str(total)})

    schemas.Alarm(**res.json()[0])
    assert len(res.json()) == total
    assert res.status_code == status.HTTP_200_OK


def test_read_alarm(client: TestClient, test_alarm: schemas.Alarm):
    
    res = client.get(f"/sites-man-api/alarms/{test_alarm.id}")

    res_alarm = schemas.Alarm(**res.json())
    assert res.status_code == status.HTTP_200_OK
    assert res_alarm.id == test_alarm.id
    assert res_alarm.description == test_alarm.description
    

def test_read_alarm_invalid_id(client: TestClient, test_alarm: schemas.Alarm):

    invalid_id = test_alarm.id + 999

    res = client.get(f"/sites-man-api/properties/{invalid_id}")

    assert res.status_code == status.HTTP_404_NOT_FOUND 


def test_update_alarm(client: TestClient, test_alarm: schemas.Alarm, test_properties: list[schemas.Property]):
    
    new_property = test_properties[-1]
    
    id = test_alarm.id
    new_property_id = new_property.id
    new_description = "test_update"
 
    res = client.put(f"/sites-man-api/alarms/{id}", params={"new_property_id": str(new_property_id), "new_description": new_description})

    print(res.json())
    res_alarm = schemas.Alarm(**res.json())

    assert res_alarm.property_id == new_property_id
    assert res_alarm.description == "test_update"
    assert res.status_code == status.HTTP_200_OK


def test_update_alarm_invalid_property_id(client: TestClient, test_alarm: schemas.Alarm, test_properties: list[schemas.User]):

    new_property = test_properties[-1]

    id = test_alarm.id
    new_property_id = new_property.id + 999

    res = client.put(f"/sites-man-api/alarms/{id}", params={"new_property_id": new_property_id})

    assert res.status_code == status.HTTP_404_NOT_FOUND


def test_update_alarm_no_id_no_desc(client: TestClient, test_alarm: schemas.Alarm):

    id = test_alarm.id

    res = client.put(f"/sites-man-api/alarms/{id}", params={"new_description": "", "new_property_id": 0})

    print(res.json())
    res_alarm = schemas.Alarm(**res.json())
    assert res_alarm.property_id == test_alarm.property_id
    assert res_alarm.description == test_alarm.description
    assert res.status_code == status.HTTP_200_OK


def test_delete_valid_alarm(client: TestClient, test_alarm: schemas.Alarm):
    
    id = test_alarm.id
    res = client.delete(f"/sites-man-api/alarms/{id}")

    assert res.status_code == status.HTTP_204_NO_CONTENT


def test_delete_invalid_alarm_id(client: TestClient, test_alarm: schemas.Alarm):
    
    id = test_alarm.id + 999
    res = client.delete(f"/sites-man-api/alarms/{id}")

    assert res.status_code == status.HTTP_404_NOT_FOUND