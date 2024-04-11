from src.settings import TEST
from src.settings.database import AsyncScopedSession


class AsyncSqlAlchemyUnitOfWork:

    def __init__(self):
        session = AsyncScopedSession()
        self._session = session

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        try:
            if exc_type is None:
                await self._session.commit()
            else:
                await self._session.rollback()
        finally:
            await self._session.close()

        # https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html#sqlalchemy.ext.asyncio.async_scoped_session.remove
        if not TEST:
            await AsyncScopedSession.remove()
