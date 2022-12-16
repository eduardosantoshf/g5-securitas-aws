import pytest
from src.config import settings
from fastapi.testclient import TestClient
from fastapi_keycloak import OIDCUser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.db.database import get_db
from src.models.models import Base
from tests.conf_idp import setup_test_idp
import src.models.schemas as schemas
from tests.conf_idp import MockOIDCUser 



SQLALCHEMY_DATABASE_URL = f'mariadb+mariadbconnector://{settings.MARIADB_USER}:{settings.MARIADB_PASSWORD}' \
    f'@{settings.MARIADB_HOST}:{settings.MARIADB_PORT}/{settings.MARIADB_DATABASE}'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=False
)

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(autouse=True, scope="function")
def setup_idp(monkeypatch, mocker):
    setup_test_idp(monkeypatch, mocker)


@pytest.fixture(autouse=True, scope="function")
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="function")
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    from src.main import app
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


@pytest.fixture(scope="function")
def test_user(client: TestClient) -> OIDCUser:
    MockOIDCUser().inject_mocked_oidc_user(
        id="1111-1111-1111-1111",
        username="ttt@ttt.com",
        roles=["g5-admin"]
    )

    return MockOIDCUser().get_mocked_oidc_user()


@pytest.fixture(scope="function")
def test_users(client: TestClient) -> list[OIDCUser]:
    users = []

    MockOIDCUser().inject_mocked_oidc_user(
        id="2222-2222-2222-2222",
        username="qqq@qqq.com",
        roles=["g5-admin"]
    )
    users.append(MockOIDCUser().get_mocked_oidc_user())

    MockOIDCUser().inject_mocked_oidc_user(
        id="3333-3333-3333-3333",
        username="www@www.com",
        roles=["g5-admin"]
    )
    users.append(MockOIDCUser().get_mocked_oidc_user())

    MockOIDCUser().inject_mocked_oidc_user(
        id="4444-4444-4444-4444",
        username="eee@eee.com",
        roles=["g5-admin"]
    )
    users.append(MockOIDCUser().get_mocked_oidc_user())

    MockOIDCUser().inject_mocked_oidc_user(
        id="5555-5555-5555-5555",
        username="rrr@rrr.com",
        roles=["g5-admin"]
    )
    users.append(MockOIDCUser().get_mocked_oidc_user())

    return users


@pytest.fixture(scope="function")
def test_property(client: TestClient, test_user: OIDCUser) -> schemas.Property:
    post_body = {
        "address": "Vila Nova"
    }
    res = client.post("/sites-man-api/properties/", params={"owner_id": str(test_user.sub)}, json=post_body)

    new_property = schemas.Property(**res.json())

    return new_property


@pytest.fixture(scope="function")
def test_properties(client: TestClient, test_user: OIDCUser) -> list[schemas.Property]:

    properties = []

    post_body = {"address": "address1"}
    res = client.post("/sites-man-api/properties/", params={"owner_id": str(test_user.sub)}, json=post_body)
    properties.append(schemas.Property(**res.json()))

    post_body = {"address": "address2"}
    res = client.post("/sites-man-api/properties/", params={"owner_id": str(test_user.sub)}, json=post_body)
    properties.append(schemas.Property(**res.json()))

    post_body = {"address": "address3"}
    res = client.post("/sites-man-api/properties/", params={"owner_id": str(test_user.sub)}, json=post_body)
    properties.append(schemas.Property(**res.json()))

    return properties


@pytest.fixture(scope="function")
def test_alarm(client: TestClient, test_property: schemas.Property) -> schemas.Alarm:
    
    post_body = {
        "description": "test_description"
    }
    res = client.post("/sites-man-api/alarms/", params={"property_id": str(test_property.id)}, json=post_body)

    new_alarm = schemas.Alarm(**res.json())

    return new_alarm


@pytest.fixture(scope="function")
def test_alarms(client: TestClient, test_property: schemas.Property) -> list[schemas.Alarm]:
    alarms = []

    post_body = {"description": "test_alarm1"}
    res = client.post("/sites-man-api/alarms/", params={"property_id": str(test_property.id)}, json=post_body)
    alarms.append(schemas.Alarm(**res.json()))

    post_body = {"description": "test_alarm2"}
    res = client.post("/sites-man-api/alarms/", params={"property_id": str(test_property.id)}, json=post_body)
    alarms.append(schemas.Alarm(**res.json()))

    post_body = {"description": "test_alarm3"}
    res = client.post("/sites-man-api/alarms/", params={"property_id": str(test_property.id)}, json=post_body)
    alarms.append(schemas.Alarm(**res.json()))

    return alarms


@pytest.fixture(scope="function")
def test_intrusion(client: TestClient, test_user: OIDCUser, test_property: schemas.Property) -> schemas.Intrusion:

    user_id = test_user.sub
    property_id = test_property.id
    post_body = {
        "description": "intrusion_1: Monday afternoon",
        "datetime": "7/11/2022 - 14:17h"
    }

    res = client.post("/sites-man-api/intrusions/", params={"user_id": user_id, "property_id": property_id}, json=post_body)

    new_intrusion = schemas.Intrusion(**res.json())

    return new_intrusion


@pytest.fixture(scope="function")
def test_intrusions(client: TestClient, test_user: OIDCUser) -> list[schemas.Intrusion]:
    intrusions = []

    post_body = {"description": "test_intrusion1", "datetime": "13/12/2022 - 13:23h"}
    res = client.post("/sites-man-api/intrusions/", params={"user_id": str(test_user.sub)}, json=post_body)
    intrusions.append(schemas.Intrusion(**res.json()))

    post_body = {"description": "test_intrusion2", "datetime": "13/12/2022 - 14:23h"}
    res = client.post("/sites-man-api/intrusions/", params={"user_id": str(test_user.sub)}, json=post_body)
    intrusions.append(schemas.Intrusion(**res.json()))

    post_body = {"description": "test_intrusion3", "datetime": "13/12/2022 - 15:23h"}
    res = client.post("/sites-man-api/intrusions/", params={"user_id": str(test_user.sub)}, json=post_body)
    intrusions.append(schemas.Intrusion(**res.json()))

    return intrusions


@pytest.fixture(scope="function")
def test_camera(client: TestClient, test_property: schemas.Property) -> schemas.Camera:
    
    post_body = {
        "description": "test_description"
    }
    res = client.post("/sites-man-api/cameras/", params={"property_id": str(test_property.id)}, json=post_body)

    new_camera = schemas.Camera(**res.json())

    return new_camera


@pytest.fixture(scope="function")
def test_cameras(client: TestClient, test_property: schemas.Property) -> list[schemas.Camera]:
    cameras = []

    post_body = {"description": "test_camera1"}
    res = client.post("/sites-man-api/cameras/", params={"property_id": str(test_property.id)}, json=post_body)
    cameras.append(schemas.Camera(**res.json()))

    post_body = {"description": "test_camera2"}
    res = client.post("/sites-man-api/cameras/", params={"property_id": str(test_property.id)}, json=post_body)
    cameras.append(schemas.Camera(**res.json()))

    post_body = {"description": "test_camera3"}
    res = client.post("/sites-man-api/cameras/", params={"property_id": str(test_property.id)}, json=post_body)
    cameras.append(schemas.Camera(**res.json()))

    return cameras