from pathlib import Path

from pydantic import BaseSettings


class Settings(BaseSettings):
    BASE_DIR: Path = Path(__file__).parent.parent
    DEBUG: bool = True

    APP_TITLE: str = 'Api'
    APP_DESC: str = 'desc'
    APP_VERSION: str = '1.0'
    DATABASE_URI = 'sqlite://db.sqlite'


settings = Settings()
