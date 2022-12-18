from src.models import schemas
from fastapi.testclient import TestClient
from fastapi import status
from fastapi_keycloak.model import OIDCUser, KeycloakUser
import pytest

from tests.conf_idp import setup_test_idp


def test_read_users_shouldGetUsers(test_users: list[OIDCUser], client: TestClient):
    # Act
    res = client.get(
        "/sites-man-api/users/")

    # Assert
    KeycloakUser(**res.json()[0])
    assert len(res.json()) == len(test_users) + 1 # +1 represents the user with id 1111-1111-...... thats already in the mock db
    assert res.status_code == status.HTTP_200_OK

def test_read_user_shouldGetUser(test_users: list[OIDCUser], client: TestClient):
    # Arrange
    test_user = test_users[-1]
    id = test_user.sub

    # Act
    res = client.get(f"/sites-man-api/users/{id}")

    # Assert
    resp_user = KeycloakUser(**res.json())
    assert resp_user.id == test_user.sub
    assert res.status_code == status.HTTP_200_OK

def test_read_user_userNotFound(test_user: OIDCUser, client: TestClient):
    # Arrange
    invalid_id = "1234-1234-1234-1234"

    # Act
    res = client.get(f"/sites-man-api/users/{invalid_id}")

    print(res.json())
    # Assert
    assert res.status_code == status.HTTP_404_NOT_FOUND

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