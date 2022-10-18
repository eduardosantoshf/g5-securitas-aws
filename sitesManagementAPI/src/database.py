from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings

# USER = "root"
# PASSWORD = "pass123"
# HOST = "db"
# PORT = 3306
# DATABASE = "site_man_db"

USER = settings.MARIADB_USER_NAME
PASSWORD = settings.MARIADB_USER_PASSWORD
HOST = settings.MARIADB_HOST
PORT = settings.MARIADB_PORT
DATABASE = settings.MARIADB_DATABASE

while True:
    try:
        SQLALCHEMY_DATABASE_URL = f'mariadb+mariadbconnector://{settings.MARIADB_USER_NAME}:{settings.MARIADB_USER_PASSWORD}' \
                                  f'@{settings.MARIADB_HOST}:{settings.MARIADB_PORT}/{settings.MARIADB_DATABASE}'

        engine = create_engine(
            SQLALCHEMY_DATABASE_URL, echo=True
        )

        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        break
    except Exception:
        print("Failed to connect to database")

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()