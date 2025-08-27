from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = "sqlite+aiosqlite:///./database.db"


settings = Settings()
