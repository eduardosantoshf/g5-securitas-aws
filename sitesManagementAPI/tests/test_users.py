from src.models import schemas
from fastapi.testclient import TestClient
from fastapi import status
from fastapi_keycloak.model import OIDCUser, KeycloakUser
import pytest

from tests.conf_idp import setup_test_idp

# def test_createUserValid(client: TestClient):
#     # Arrange
#     post_body = {"name": "joao",
#                  "email": "joao@gmail.com",
#                  "address": "myaddress"}
#     # Act
#     res = client.post("/sites-man-api/users/", json=post_body)

#     # Assert
#     new_user = schemas.User(**res.json())
#     assert new_user.email == "joao@gmail.com"
#     assert res.status_code == status.HTTP_201_CREATED

# def test_create_user_alreadyRegisteredEmail(test_user: schemas.User, client: TestClient):
#     # Arrange
#     post_body = {"name": "joao",
#                  "email": test_user.email,
#                  "address": "myaddress"}

#     # Act
#     res = client.post("/sites-man-api/users/", json=post_body)

#     # Assert
#     assert res.status_code == status.HTTP_400_BAD_REQUEST
#     assert res.json().get("detail") == "Email already registered"

@pytest.mark.parametrize(
    "skip, limit, total", [
        (1, 2, 2),
        (0, 3, 3),
    ])
def test_read_users_shouldGetUsers(test_users: list[OIDCUser], client: TestClient,
                                   skip: int, limit: int, total: int):
    # Act
    res = client.get(
        "/sites-man-api/users/", params={"skip": str(skip), "limit": str(limit)})

    # Assert
    OIDCUser(**res.json()[0])
    assert len(res.json()) == total
    assert res.status_code == status.HTTP_200_OK

def test_read_user_shouldGetUser(test_users: list[OIDCUser], client: TestClient):
    # Arrange
    test_user = test_users[-1]
    id = test_user.sub

    # Act
    res = client.get(f"/sites-man-api/users/{id}")

    # Assert
    resp_user = OIDCUser(**res.json())
    assert resp_user.sub == test_user.sub
    assert res.status_code == status.HTTP_200_OK

def test_read_user_userNotFound(test_user: OIDCUser, client: TestClient):
    # Arrange
    id = "1234-1234-1234-1234"

    # Act
    res = client.get(f"/sites-man-api/users/{id}")

    # Assert
    assert res.status_code == status.HTTP_404_NOT_FOUND

# def test_update_user_shouldUpdate(test_user: schemas.User, client: TestClient):
#     # Arrange
#     id = test_user.id
#     put_body = {"name": "newName",
#                  "email": "newEmail@gmail.com",
#                  "address": "newAddress"}
#     # Act
#     res = client.put(f"/sites-man-api/users/{id}", json=put_body)

#     #Assert
#     updated_user = schemas.User(**res.json())
#     assert updated_user.name == put_body["name"]
#     assert updated_user.email == put_body["email"]
#     assert updated_user.address == put_body["address"]
#     assert res.status_code == status.HTTP_200_OK

# def test_update_user_notFound(test_user: schemas.User, client: TestClient):
#     # Arrange
#     id = test_user.id + 100

#     # Act
#     res = client.get(f"/sites-man-api/users/{id}")

#     # Assert
#     assert res.status_code == status.HTTP_404_NOT_FOUND

# def test_delete_user_shouldDelete(test_user: schemas.User, client: TestClient):
#     # Arrange
#     id = test_user.id

#     # Act
#     res = client.delete(f"/sites-man-api/users/{id}")

#     #Assert
#     assert res.status_code == status.HTTP_204_NO_CONTENT

# def test_delete_user_notFound(test_user: schemas.User, client: TestClient):
#     # Arrange
#     id = test_user.id + 100

#     # Act
#     res = client.delete(f"/sites-man-api/users/{id}")

#     # Assert
#     assert res.status_code == status.HTTP_404_NOT_FOUND

def test_read_users_cameras(test_user: OIDCUser, test_cameras: schemas.Camera, client: TestClient):

    id = test_user.sub

    res = client.get(f"/sites-man-api/users/{id}/cameras")

    assert len(res.json()) == len(test_cameras)
    assert res.status_code == status.HTTP_200_OK

def test_read_users_cameras_invalid_id(test_user: OIDCUser, client: TestClient):

    id = "1234-1234-1234-1234"

    res = client.get(f"/sites-man-api/users/{id}/cameras")

    assert res.status_code == status.HTTP_404_NOT_FOUND

def test_read_users_no_cameras(test_user: OIDCUser, client: TestClient):

    id = test_user.sub

    res = client.get(f"/sites-man-api/users/{id}/cameras")

    assert res.json() == []

def test_read_users_alarms(test_user: OIDCUser, test_alarms: schemas.Alarm, client: TestClient):

    id = test_user.sub

    res = client.get(f"/sites-man-api/users/{id}/alarms")

    assert len(res.json()) == len(test_alarms)
    assert res.status_code == status.HTTP_200_OK

def test_read_users_alarms_invalid_id(test_user: OIDCUser, client: TestClient):

    id = "1234-1234-1234-1234"

    res = client.get(f"/sites-man-api/users/{id}/alarms")

    assert res.status_code == status.HTTP_404_NOT_FOUND

def test_read_users_no_alarms(test_user: OIDCUser, client: TestClient):

    id = test_user.sub

    res = client.get(f"/sites-man-api/users/{id}/alarms")

    assert res.json() == []