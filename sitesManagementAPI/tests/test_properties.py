from fastapi.testclient import TestClient
from fastapi import status
from fastapi_keycloak import OIDCUser
import pytest

from src.models import schemas
from tests.conf_idp import setup_test_idp


def test_create_valid_property(client: TestClient, test_user: OIDCUser):
    
    post_body = {"address": "test_address"}
    owner_id = test_user.sub

    res = client.post("/sites-man-api/properties/", params={"owner_id": str(owner_id)}, json=post_body)

    new_property = schemas.Property(**res.json())
    assert new_property.address == "test_address"
    assert res.status_code == status.HTTP_201_CREATED


def test_create_existing_property(client: TestClient, test_property: schemas.Property, test_user: OIDCUser):
    
    post_body = {"address": test_property.address}
    
    res = client.post("/sites-man-api/properties/", params={"owner_id": str(test_user.sub)}, json=post_body)

    assert res.status_code == status.HTTP_400_BAD_REQUEST
    assert res.json().get("detail") == "Property already registred"


def test_create_property_non_existing_owner(client: TestClient, test_user: OIDCUser):

    owner_id = "1234-1234-1234-1234"
    post_body = {"address": "test_address"}

    res = client.post("/sites-man-api/properties/", params={"owner_id": str(owner_id)}, json=post_body)

    assert res.status_code == status.HTTP_404_NOT_FOUND
    assert res.json().get("detail") == f"User with id {owner_id} not found"


@pytest.mark.parametrize(
    "skip, limit, total", [
        (1, 2, 2),
        (0, 3, 3),
    ])
def test_read_properties(client: TestClient, test_properties: list[schemas.Property],
                         skip: int, limit: int, total: int):

    res = client.get(f"/sites-man-api/properties/", params={"skip": str(skip), "limit": str(limit), "total": str(total)})

    schemas.Property(**res.json()[0])
    assert len(res.json()) == total
    assert res.status_code == status.HTTP_200_OK


def test_read_property(client: TestClient, test_property: schemas.Property):
    
    res = client.get(f"/sites-man-api/properties/{test_property.id}")

    res_property = schemas.Property(**res.json())
    assert res.status_code == status.HTTP_200_OK
    assert res_property.id == test_property.id
    assert res_property.address == test_property.address   


def test_read_property_invalid_id(client: TestClient, test_property: schemas.Property):
    
    invalid_id = test_property.id + 999

    res = client.get(f"/sites-man-api/properties/{invalid_id}")

    assert res.status_code == status.HTTP_404_NOT_FOUND


def test_update_property(client: TestClient, test_property: schemas.Property, test_users: list[OIDCUser]):
    
    new_owner = test_users[-1]
    id = test_property.id
    new_owner_id = new_owner.sub
    new_address = "Test address"

    res = client.put(f"/sites-man-api/properties/{id}", params={"new_owner_id": str(new_owner_id), "new_address": str(new_address)})

    print(res.json())
    res_property = schemas.Property(**res.json())

    assert res_property.owner_id == new_owner_id
    assert res_property.address == new_address
    assert res.status_code == status.HTTP_200_OK


def test_update_property_invalid_owner_id(client: TestClient, test_property: schemas.Property, test_users: list[OIDCUser]):

    new_owner = test_users[-1]
    id = test_property.id
    new_owner_id = "1234-1234-1234-1234"

    res = client.put(f"/sites-man-api/properties/{id}", params={"new_owner_id": new_owner_id})

    assert res.status_code == status.HTTP_404_NOT_FOUND
    assert res.json().get("detail") == f"User with id {new_owner_id} not found"


def test_update_property_invalid_new_address(client: TestClient, test_property: schemas.Property, test_users: list[OIDCUser]):
    
    new_owner = test_users[-1]
    id = test_property.id
    new_address = test_property.address

    res = client.put(f"/sites-man-api/properties/{id}", params={"new_address": new_address})

    assert res.status_code == status.HTTP_400_BAD_REQUEST
    assert res.json().get("detail") == f'Property already registred at specified address'


def test_delete_valid_property(client: TestClient, test_property: schemas.Property):
    
    id = test_property.id
    res = client.delete(f"/sites-man-api/properties/{id}")

    assert res.status_code == status.HTTP_204_NO_CONTENT


def test_delete_invalid_property_id(client: TestClient, test_property: schemas.Property):
    
    id = test_property.id + 999
    res = client.delete(f"/sites-man-api/properties/{id}")

    assert res.status_code == status.HTTP_404_NOT_FOUND