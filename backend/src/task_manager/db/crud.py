from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from task_manager.db.models import Task as DbTask
from task_manager.models import Task as ApiTask, TaskStatus
from task_manager.db.connection import connection

def convert_to_db_task(task: ApiTask) -> DbTask:
    return DbTask(
            id=task.id,
            title=task.title,
            description=task.description,
            status=task.status.value,
            progress=task.progress
        )

def convert_from_db_task(task: DbTask | None) -> ApiTask | None:
    if task:
        return ApiTask(
            id=task.id,
            title=task.title,
            description=task.description,
            status=TaskStatus(task.status),
            progress=task.progress
        )
    return task


async def create_task(db_uri: str, task: ApiTask) -> ApiTask:
    async with connection(db_uri) as db:
        db_task = convert_to_db_task(task)
        db.add(db_task)
        await db.commit()
        await db.refresh(db_task)
        return convert_from_db_task(db_task)


async def read_task(db_uri: str, task_id: str) -> ApiTask | None:
    async with connection(db_uri) as db:
        task = await db.execute(select(DbTask).where(DbTask.id == task_id))
        return convert_from_db_task(task.scalar_one_or_none())


async def read_tasks(db_uri: str) -> list[ApiTask]:
    async with connection(db_uri) as db:
        tasks = await db.execute(select(DbTask))
        return [convert_from_db_task(t) for t in tasks.scalars().all()]


async def update_task(db_uri: str, task: ApiTask) -> ApiTask:
    async with connection(db_uri) as db:
        db_task = convert_to_db_task(task)
        await db.execute(update(DbTask).where(DbTask.id == task.id).values(**task.model_dump()))
        await db.commit()
        return task


async def delete_task(db_uri: str, task_id: str) -> None:
    async with connection(db_uri) as db:
        await db.execute(delete(DbTask).where(DbTask.id == task_id))
        await db.commit()













