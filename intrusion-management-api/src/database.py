from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.config import settings

while True:
    try:
        SQLALCHEMY_DATABASE_URL = f'mariadb+mariadbconnector://{settings.MARIADB_USER}:{settings.MARIADB_PASSWORD}' \
                                  f'@{settings.MARIADB_HOST}:{settings.MARIADB_PORT}/{settings.MARIADB_DATABASE}'

        print(SQLALCHEMY_DATABASE_URL)
        engine = create_engine(
            SQLALCHEMY_DATABASE_URL, echo=True,
            pool_pre_ping=True
            
        )

        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        break
    except Exception as e:
        print("Failed to connect to database: ", e)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()