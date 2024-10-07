from typing import ClassVar
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

DBBaseModel = declarative_base()

class Settings(BaseSettings):
    AP_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://postgres:postgresql@localhost:5432/faculdade"
    DBBaseModel: ClassVar = DBBaseModel  # Anotando como ClassVar

    class Config:
        case_sensitive = True

settings = Settings()
