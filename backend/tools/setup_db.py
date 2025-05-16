import asyncio
from task_manager.db.connection import get_db_connection
from task_manager.db.models import Base
from task_manager.config import settings

async def setup_db():
    engine, async_session = get_db_connection(settings.DATABASE_URL)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(setup_db())