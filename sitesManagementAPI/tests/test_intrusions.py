from fastapi.testclient import TestClient
from fastapi import status
import pytest

from src.models import schemas


def test_create_valid_intrusion(client: TestClient, test_user: schemas.User, test_property: schemas.Property):
    
    user_id = test_user.id
    property_id = test_property.id
    post_body = {
        "description": "intrusion_1: main building",
        "datetime": "11/11/2022 - 13:34h"
    }

    res = client.post("/sites-man-api/intrusions/", params={"user_id": user_id, "property_id": property_id}, json=post_body)

    new_intrusion = schemas.Intrusion(**res.json())
    assert new_intrusion.description == post_body["description"]
    assert new_intrusion.user_id == user_id
    assert new_intrusion.property_id == property_id
    assert res.status_code == status.HTTP_201_CREATED


def test_create_intrusion_invalid_user(client: TestClient, test_user: schemas.User):

    user_id = test_user.id + 999
    post_body = {
        "description": "test_intrusion",
        "datetime": "14/11/2022 - 16:31h"
    }

    res = client.post("/sites-man-api/intrusions/", params={"user_id": user_id}, json=post_body)

    assert res.status_code == status.HTTP_404_NOT_FOUND
    assert res.json().get("detail") == f"User with id {user_id} not found"

def test_create_intrusion_invalid_property(client: TestClient, test_user: schemas.User, test_property: schemas.Property):

    user_id = test_user.id
    property_id = test_property.id + 999
    post_body = {
        "description": "test_intrusion",
        "datetime": "14/11/2022 - 16:31h"
    }

    res = client.post("/sites-man-api/intrusions/", params={"user_id": user_id, "property_id": property_id}, json=post_body)

    assert res.status_code == status.HTTP_404_NOT_FOUND
    assert res.json().get("detail") == f"Property with id {property_id} not found"


@pytest.mark.parametrize(
    "skip, limit, total", [
        (1, 2, 2),
        (0, 3, 3),
    ])
def test_read_intrusions(client: TestClient, test_intrusions: list[schemas.Intrusion],
                         skip: int, limit: int, total: int):

    res = client.get(f"/sites-man-api/intrusions/", params={"skip": str(skip), "limit": str(limit), "total": str(total)})

    schemas.Intrusion(**res.json()[0])
    assert len(res.json()) == total
    assert res.status_code == status.HTTP_200_OK


def test_read_intrusion(client: TestClient, test_intrusion: schemas.Intrusion):
    
    res = client.get(f"/sites-man-api/intrusions/{test_intrusion.id}")

    res_intrusion = schemas.Intrusion(**res.json())
    assert res.status_code == status.HTTP_200_OK
    assert res_intrusion.id == test_intrusion.id
    assert res_intrusion.user_id == test_intrusion.user_id
    assert res_intrusion.description == test_intrusion.description
    

def test_read_intrusion_invalid_id(client: TestClient, test_intrusion: schemas.Intrusion):

    invalid_id = test_intrusion.id + 999

    res = client.get(f"/sites-man-api/properties/{invalid_id}")

    assert res.status_code == status.HTTP_404_NOT_FOUND 


def test_update_intrusion(client: TestClient, test_intrusion: schemas.Intrusion, test_users: list[schemas.User], test_property: schemas.Property):
    
    new_user = test_users[-1]
    
    id = test_intrusion.id
    new_user_id = new_user.id
    new_property_id = test_property.id
    put_body = {
        "description": "new_description",
        "datetime": "new_datetime"
    }
 
    res = client.put(f"/sites-man-api/intrusions/{id}", params={"new_user_id": str(new_user_id), "new_property_id": str(new_property_id)}, json=put_body)

    res_intrusion = schemas.Intrusion(**res.json())

    assert res_intrusion.user_id == new_user_id
    assert res_intrusion.property_id == new_property_id
    assert res_intrusion.description == "new_description"
    assert res_intrusion.datetime == "new_datetime"
    assert res.status_code == status.HTTP_200_OK


def test_update_intrusion_invalid_user_id(client: TestClient, test_intrusion: schemas.Intrusion, test_user: schemas.User):

    id = test_intrusion.id
    new_user_id = test_user.id + 999
    put_body = {
        "description": "new_description",
        "datetime": "new_datetime"
    }

    res = client.put(f"/sites-man-api/intrusions/{id}", params={"new_user_id": str(new_user_id)}, json=put_body)

    assert res.status_code == status.HTTP_404_NOT_FOUND
    assert res.json().get("detail") == f"User with id {new_user_id} not found"


def test_update_intrusion_invalid_property_id(client: TestClient, test_intrusion: schemas.Intrusion, test_properties: list[schemas.Property]):

    new_property = test_properties[-1]

    id = test_intrusion.id
    new_property_id = new_property.id + 999
    put_body = {
        "description": test_intrusion.description,
        "datetime": test_intrusion.datetime
    }

    res = client.put(f"/sites-man-api/intrusions/{id}", params={"new_property_id": str(new_property_id)}, json=put_body)

    assert res.status_code == status.HTTP_404_NOT_FOUND
    assert res.json().get("detail") == f"Property with id {new_property_id} not found"


def test_update_intrusion_no_prop_id_no_user_id(client: TestClient, test_intrusion: schemas.Intrusion):

    id = test_intrusion.id
    put_body = {
        "description": test_intrusion.description,
        "datetime": test_intrusion.datetime
    }

    res = client.put(f"/sites-man-api/intrusions/{id}", json=put_body)

    print(res.json())
    res_intrusion = schemas.Intrusion(**res.json())
    assert res_intrusion.user_id == test_intrusion.user_id
    assert res_intrusion.property_id == test_intrusion.property_id
    assert res.status_code == status.HTTP_200_OK


def test_delete_valid_intrusion(client: TestClient, test_intrusion: schemas.Intrusion):
    
    id = test_intrusion.id
    res = client.delete(f"/sites-man-api/intrusions/{id}")

    assert res.status_code == status.HTTP_204_NO_CONTENT


def test_delete_invalid_intrusion_id(client: TestClient, test_intrusion: schemas.Intrusion):
    
    id = test_intrusion.id + 999
    res = client.delete(f"/sites-man-api/intrusions/{id}")

    assert res.status_code == status.HTTP_404_NOT_FOUND