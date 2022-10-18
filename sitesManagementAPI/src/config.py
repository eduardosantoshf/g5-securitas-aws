from pydantic import BaseSettings

class Settings(BaseSettings):
    MARIADB_USER_PASSWORD: str
    MARIADB_USER_NAME: str
    MARIADB_DATABASE: str
    MARIADB_HOST: str
    MARIADB_PORT: str

    class Config:
        env_file = ".env"
settings = Settings()