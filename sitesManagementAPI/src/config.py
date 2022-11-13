from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    MARIADB_USER: str = os.getenv("MARIADB_USER")
    MARIADB_PASSWORD: str = os.getenv("MARIADB_PASSWORD")
    MARIADB_DATABASE: str = os.getenv("MARIADB_DATABASE")
    MARIADB_HOST: str = os.getenv("MARIADB_HOST")
    MARIADB_PORT: str = os.getenv("MARIADB_PORT")
    
    class Config:
        env_file = ".env"

settings = Settings()