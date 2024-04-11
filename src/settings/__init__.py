import os
from functools import lru_cache
from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    SERVICE_NAME: str = 'fastapi-mysql-template'
    HOST: str = '0.0.0.0'
    PORT: int = 8221
    DOC_URL: str = '/docs'
    REDOC_URL: str = '/redocs'

    # MySQL
    MYSQL_HOST: str = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_PORT: int = os.getenv('MYSQL_PORT', 3306)  # type: ignore
    MYSQL_USERNAME: str = os.getenv('MYSQL_USERNAME', 'root')
    MYSQL_PASSWORD: str = os.getenv('MYSQL_PASSWORD', 'secret')
    MYSQL_DATABASE: str = os.getenv('MYSQL_DATABASE', 'database')
    MYSQL_CONN_TIMEOUT: int = 5000

    # SSH: DB connection option
    SSH_HOST: Optional[str] = 'ssh-host'
    SSH_PORT: Optional[int] = 25432
    SSH_USERNAME: Optional[str] = 'user'
    SSH_PASSWORD: Optional[str] = 'password'

    # AWS
    REGION_NAME: str = 'ap-northeast-1'
    S3_BUCKET_NAME: str = os.getenv('S3_BUCKET_NAME')
    S3_BUCKET_HOST: str = os.getenv('S3_BUCKET_HOST')

    # Website
    DOMAIN_NAME: str = os.getenv('DOMAIN_NAME', 'localhost')

@lru_cache()
def get_settings():
    return Settings()  # type: ignore


settings = get_settings()
