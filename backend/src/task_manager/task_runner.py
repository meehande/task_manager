import asyncio
from typing import Callable
from task_manager.models import Task, TaskStatus


def task_runner_factory(task: Task) -> Callable:
    async def run_task_async():
        print(f"Running task {task.id}")
        for i in range(30):
            if task.status == TaskStatus.CANCELLED:
                return
            if task.status == TaskStatus.PAUSED:
                await asyncio.sleep(1)
                continue
            await asyncio.sleep(1)
            task.progress = (i + 1) / 30 * 100
        task.status = TaskStatus.COMPLETED

    return run_task_async
