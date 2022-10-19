from src import schemas
from src.main import app
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config import settings
from src.database import get_db
from src.models import Base
import pytest

SQLALCHEMY_DATABASE_URL = f'mariadb+mariadbconnector://{settings.MARIADB_USER}:{settings.MARIADB_PASSWORD}' \
    f'@{settings.MARIADB_HOST}:{settings.MARIADB_PORT}/{settings.MARIADB_DATABASE}'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=True
)

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def session():
    print(Base.metadata.tables.values())
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture()
def client(session):
    def override_get_db():

        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


def test_create_user(client: TestClient):
    res = client.post("/users/", json={"name": "joao",
                                       "email": "joao@gmail.com",
                                       "address": "myaddress"})
    new_user = schemas.UserCreate(**res.json())
    assert new_user.email == "joao@gmail.com"
    assert res.status_code == 201
