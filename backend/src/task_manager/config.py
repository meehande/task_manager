from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    DATABASE_URL: str = Field("postgresql+asyncpg://postgres:postgres@localhost:5432/postgres", env="DATABASE_URL")


settings = Settings()