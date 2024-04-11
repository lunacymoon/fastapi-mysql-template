import pytest
from httpx import AsyncClient
from sqlalchemy import event

from main import app
from src.settings import settings
from src.settings.database import AsyncScopedSession, async_engine, get_session


@pytest.fixture(scope='session')
def anyio_backend():
    return 'asyncio'


@pytest.fixture(scope='function')
async def session():
    async with async_engine.connect() as conn:
        await conn.begin()
        await conn.begin_nested()
        async_session = AsyncScopedSession(bind=conn)

        @event.listens_for(async_session.sync_session, 'after_transaction_end')
        def end_savepoint(sess, transaction):
            if conn.closed:
                return
            if not conn.in_nested_transaction():
                conn.sync_connection.begin_nested()

        yield async_session

    await async_engine.dispose()


@pytest.fixture(scope='session')
async def client():
    async with AsyncClient(app=app, base_url=f'http://testserver/{settings.SERVICE_NAME}') as ac:
        yield ac


@pytest.fixture(autouse=True)
async def override_session(session):  # pylint: disable=redefined-outer-name
    async def get_test_session():
        return session

    app.dependency_overrides[get_session] = get_test_session
