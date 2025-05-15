from fastapi import APIRouter, HTTPException
from task_manager.models import Task, TaskStatus
from task_manager.routes.api import CreateTaskRequest
from typing import Dict
import asyncio
import uuid
from task_manager.task_runner import task_runner_factory

router = APIRouter(prefix="/v1/tasks")

# todo: replace with db
tasks: Dict[str, Task] = {}


@router.post("/", response_model=Task)
async def create_task(request: CreateTaskRequest) -> Task:
    """Create a new task."""
    task_id = str(uuid.uuid4())
    task = Task(id=task_id, title=request.title, description=request.description)
    tasks[task_id] = task
    return task


@router.get("/{task_id}", response_model=Task)
async def get_task(task_id: str) -> Task:
    """Get task by ID."""
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]


@router.post("/{task_id}/run")
async def run_task(task_id: str) -> Task:
    """Run a task."""
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    task = tasks[task_id]
    if task.status == TaskStatus.IN_PROGRESS:
        raise HTTPException(status_code=400, detail="Task is already running")

    task.status = TaskStatus.IN_PROGRESS
    # Simulate long-running task
    task_runner = task_runner_factory(task)

    asyncio.create_task(task_runner())
    return task


@router.post("/{task_id}/cancel")
async def cancel_task(task_id: str) -> Task:
    """Cancel a task."""
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    task = tasks[task_id]
    if task.status not in [TaskStatus.IN_PROGRESS, TaskStatus.PAUSED]:
        raise HTTPException(status_code=400, detail="Task is not running or paused")

    task.status = TaskStatus.CANCELLED
    return task


@router.post("/{task_id}/pause")
async def pause_task(task_id: str) -> Task:
    """Pause a running task."""
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    task = tasks[task_id]
    if task.status != TaskStatus.IN_PROGRESS:
        raise HTTPException(status_code=400, detail="Task is not running")
    # todo: this should do some sort of pause logic to save current state to be resumed
    task.status = TaskStatus.PAUSED
    return task


@router.post("/{task_id}/resume")
async def resume_task(task_id: str) -> Task:
    """Resume a paused task."""
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    task = tasks[task_id]
    if task.status != TaskStatus.PAUSED:
        raise HTTPException(status_code=400, detail="Task is not paused")
    task.status = TaskStatus.IN_PROGRESS
    return task
