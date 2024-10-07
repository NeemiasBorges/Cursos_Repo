from typing import List
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from typing import ClassVar

DBBaseModel = declarative_base()

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:postgresql@localhost:5432/faculdade'
    DBBaseModel: ClassVar = DBBaseModel  

    JWT_SECRET: str = 'RSNe4FVYLg29HE4-Y5KN4FYOfDjP2ZgMEVEPZrfK8Zs'
    ALGORITHM: str = 'HS256'
    ACESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True

settings = Settings = Settings()   