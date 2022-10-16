from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 
#    User*: test
#    Password*: 123
#    Host: 127.0.0.1 (localhost)
#    Port: 3306
#    Default database: test
#
SQLALCHEMY_DATABASE_URL = "mariadb+mariadbconnector://root:mypass@127.0.0.1:3306/test"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()