
from contextlib import asynccontextmanager
from functools import lru_cache
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker


@lru_cache
def get_db_connection(db_uri: str):
    engine = create_async_engine(db_uri)
    async_session = async_sessionmaker(engine, expire_on_commit=False)
    return engine, async_session


@asynccontextmanager
async def connection(db_uri: str):
    try:
        engine, async_session = get_db_connection(db_uri)
        db = async_session()
        yield db
    finally:
        await db.close()
