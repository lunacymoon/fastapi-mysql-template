import os
from asyncio import current_task
from typing import AsyncIterable

import sqlalchemy.orm
from sqlalchemy import MetaData, inspect
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.asyncio import AsyncSession as _AsyncSession
from sqlalchemy.ext.asyncio import async_scoped_session, create_async_engine
from sqlalchemy.future.engine import Connection
from sqlalchemy.orm import backref as _backref
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.orm import relationship as _relationship
from sqlalchemy.orm.attributes import flag_modified
from sqlalchemy.orm.session import Session
from src.settings.test import pytest_scope_func
from src.settings import settings
from src.settings.ssh_tunnel import Tunnel

from src.settings.database import (
    DATABASE_DATABASE,
    DATABASE_HOST,
    DATABASE_PASSWORD,
    DATABASE_PORT,
    DATABASE_USERNAME,
)

ENVIRONMENT = os.getenv('ENVIRONMENT', 'local')
TEST = os.getenv('TEST', '')
DEBUG = os.getenv('ENVIRONMENT', 'local')
IS_DEBUG: bool = True if DEBUG not in {'SIT', 'UAT', 'PROD'} else False

SSH_ENABLE = True if ENVIRONMENT == 'local' else False
DATABASE_USERNAME = settings.MYSQL_USERNAME
DATABASE_PASSWORD = settings.MYSQL_PASSWORD
DATABASE_HOST = settings.MYSQL_HOST if not SSH_ENABLE else '127.0.0.1'
DATABASE_PORT = settings.MYSQL_PORT if not SSH_ENABLE else Tunnel().get_local_port()
DATABASE_DATABASE = settings.MYSQL_DATABASE

db_url = URL.create(
    'mysql+aiomysql',
    username=DATABASE_USERNAME,
    password=DATABASE_PASSWORD,
    host=DATABASE_HOST,
    port=DATABASE_PORT,
    database=DATABASE_DATABASE,
    query={"charset": "utf8mb4"},
)

async_engine = create_async_engine(
    db_url,
    isolation_level='REPEATABLE READ',
    echo=IS_DEBUG,
    pool_recycle=600,
    pool_size=30,
    max_overflow=10,
    connect_args={'connect_timeout': 5},
)


class AsyncSession(_AsyncSession):  # pylint: disable=abstract-method
    def __init__(self, *args, **kargs):
        super().__init__(sync_session_class=Session, *args, **kargs)

    async def set_flag_modified(self, instance, key: str):
        flag_modified(instance, key)


AsyncScopedSession = async_scoped_session(
    sessionmaker(
        async_engine,
        expire_on_commit=False,
        autoflush=False,
        class_=AsyncSession,
    ),  # type: ignore
    scopefunc=current_task if not TEST else pytest_scope_func,
)


sqlalchemy.orm.relationship = lambda *args, **kwargs: _relationship(lazy=kwargs.pop('lazy', 'raise'), *args, **kwargs)
sqlalchemy.orm.backref = lambda *args, **kwargs: _backref(lazy=kwargs.pop('lazy', 'raise'), *args, **kwargs)


async def get_session() -> AsyncIterable[AsyncSession]:
    async with AsyncScopedSession() as session:
        yield session


def get_schema_names(conn: Connection) -> list[str]:
    inspector = inspect(conn)
    return inspector.get_schema_names()


SQLAlchemyBase = declarative_base(metadata=MetaData(schema=DATABASE_DATABASE))
