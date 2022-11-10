from src.main import app
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config import settings
from src.db.database import get_db
from src.models.models import Base
import pytest
import src.models.schemas as schemas

SQLALCHEMY_DATABASE_URL = f'mariadb+mariadbconnector://{settings.MARIADB_USER}:{settings.MARIADB_PASSWORD}' \
    f'@{settings.MARIADB_HOST}:{settings.MARIADB_PORT}/{settings.MARIADB_DATABASE}'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=False
)

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
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

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


@pytest.fixture(scope="function")
def test_user(client: TestClient) -> schemas.User:
    user_data = {"name": "Ricardo",
                 "email": "ricardocas@gmail.com",
                 "address": "Rua do francisco perdido"}
    res = client.post("/users/", json=user_data)

    new_user = schemas.User(**res.json())
    return new_user


@pytest.fixture(scope="function")
def test_users(client: TestClient) -> list[schemas.User]:
    users = []
    user_data = {"name": "Ricardo",
                 "email": "ricardao@gmail.com",
                 "address": "Rua do francisco perdido"}
    res = client.post("/users/", json=user_data)
    users.append(schemas.User(**res.json()))

    user_data = {"name": "Rui Aguiar",
                 "email": "ruiAguiar@ua.pt",
                 "address": "Praceira dos cansados"}
    res = client.post("/users/", json=user_data)
    users.append(schemas.User(**res.json()))

    user_data = {"name": "Sergio Calado",
                 "email": "sergioCaladoPJ@gmail.com",
                 "address": "Terreiro do chaço"}
    res = client.post("/users/", json=user_data)
    users.append(schemas.User(**res.json()))

    return users


@pytest.fixture(scope="function")
def test_property(client: TestClient, test_user: schemas.User) -> schemas.Property:
    post_body = {
        "address": "Vila Nova"
    }
    res = client.post("/properties/", params={"owner_id": str(test_user.id)}, json=post_body)

    new_property = schemas.Property(**res.json())

    return new_property


@pytest.fixture(scope="function")
def test_properties(client: TestClient, test_user: schemas.User) -> list[schemas.Property]:

    properties = []

    post_body = {"address": "address1"}
    res = client.post("/properties/", params={"owner_id": str(test_user.id)}, json=post_body)
    properties.append(schemas.Property(**res.json()))

    post_body = {"address": "address2"}
    res = client.post("/properties/", params={"owner_id": str(test_user.id)}, json=post_body)
    properties.append(schemas.Property(**res.json()))

    post_body = {"address": "address3"}
    res = client.post("/properties/", params={"owner_id": str(test_user.id)}, json=post_body)
    properties.append(schemas.Property(**res.json()))

    return properties


@pytest.fixture(scope="function")
def test_alarm(client: TestClient, test_property: schemas.Property) -> schemas.Alarm:
    
    post_body = {
        "description": "test_description"
    }
    res = client.post("/alarms/", params={"property_id": str(test_property.id)}, json=post_body)

    new_alarm = schemas.Alarm(**res.json())

    return new_alarm


@pytest.fixture(scope="function")
def test_alarms(client: TestClient, test_property: schemas.Property) -> list[schemas.Alarm]:

    alarms = []

    post_body = {"description": "test_alarm1"}
    res = client.post("/alarms/", params={"property_id": str(test_property.id)}, json=post_body)
    alarms.append(schemas.Alarm(**res.json()))

    post_body = {"description": "test_alarm2"}
    res = client.post("/alarms/", params={"property_id": str(test_property.id)}, json=post_body)
    alarms.append(schemas.Alarm(**res.json()))

    post_body = {"description": "test_alarm3"}
    res = client.post("/alarms/", params={"property_id": str(test_property.id)}, json=post_body)
    alarms.append(schemas.Alarm(**res.json()))

    return alarms