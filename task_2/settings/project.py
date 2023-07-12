import functools
import logging
import os

from pydantic import Field, BaseSettings
from load_dotenv import load_dotenv

load_dotenv('.env')

origins = [
    "http://127.0.0.1:8000/",
]


class Settings(BaseSettings):
    # Back-end settings
    DEBUG: bool = Field(default=False)
    SHOW_SETTINGS: bool = Field(default=False)
    HOST: str = Field(default="127.0.0.1")
    PORT: str = Field(default="8000")
    SERVER_URL: str = Field(default="http://127.0.0.1:8000/")
    DATETIME_FORMAT: str = Field(default="%Y-%m-%d %H:%M:%S")
    TRUSTED_HOSTS: list[str] = Field(default=["127.0.0.1"])
    # CORS settings
    CORS_ALLOW_CREDENTIALS: bool = Field(default=True)
    CORS_ALLOW_HEADERS: list[str] = Field(
        default=[
            "Content-Type",
            "Set-Cookie",
            "Access-Control-Allow-Headers",
            "Access-Control-Allow-Origin",
            "Authorization",
        ]
    )
    CORS_ALLOW_METHODS: list[str] = Field(
        default=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"]
    )
    CORS_ALLOW_ORIGINS: list[str] = Field(default=origins)
    # JWT tokens managements settings
    TOKENS_ACCESS_LIFETIME_SECONDS: int = Field(default=3600)  # 1 HOUR
    TOKENS_REFRESH_LIFETIME_SECONDS: int = Field(default=86400)  # 1 DAY
    TOKENS_SECRET_KEY: str = Field(default=os.environ.get("TOKENS_SECRET_KEY"))
    # Logging settings
    LOG_LEVEL: int = Field(default=logging.INFO)
    LOG_USE_COLORS: bool = Field(default=True)
    # Database settings
    DATABASE_URL: str = Field(default=os.environ.get("DATABASE_URL"))
    TEST_DATABASE_URL: str = Field(default=os.environ.get("TEST_DATABASE_URL"))


@functools.lru_cache()
def get_settings() -> Settings:
    return Settings()


Settings: Settings = get_settings()
