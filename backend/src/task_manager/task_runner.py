import asyncio
from typing import Callable
from task_manager.models import Task, TaskStatus
from task_manager.db.crud import update_task, read_task


def task_runner_factory(db_uri: str, task_id: str) -> Callable: 
    async def run_task_async():
        for i in range(30):
            print(f"in loop: {i}")
            task = await read_task(db_uri, task_id)
            if task.status == TaskStatus.CANCELLED:
                return
            if task.status == TaskStatus.PAUSED:
                await asyncio.sleep(1)
                continue
            await asyncio.sleep(1)
            task.progress = (i + 1) / 30 * 100
            await update_task(db_uri, task)
        task.status = TaskStatus.COMPLETED
        await update_task(db_uri, task)

    return run_task_async
