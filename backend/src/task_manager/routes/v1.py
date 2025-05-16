from fastapi import APIRouter, HTTPException
from task_manager.models import Task, TaskStatus
from task_manager.routes.api import CreateTaskRequest
from typing import Dict
import asyncio
import uuid
from task_manager.task_runner import task_runner_factory
from task_manager.db.crud import (
    create_task as create_task_in_db, 
    read_task, 
    read_tasks, 
    update_task)
from task_manager.config import settings
router = APIRouter(prefix="/v1/tasks")


@router.post("/", response_model=Task)
async def create_task(request: CreateTaskRequest) -> Task:
    task_id = str(uuid.uuid4())
    task = Task(id=task_id, title=request.title, description=request.description)
    task = await create_task_in_db(settings.DATABASE_URL, task)
    return task


@router.get("/{task_id}", response_model=Task)
async def get_task(task_id: str) -> Task:
    task = await read_task(settings.DATABASE_URL, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.post("/{task_id}/run")
async def run_task(task_id: str) -> Task:
    task = await read_task(settings.DATABASE_URL, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if task.status == TaskStatus.IN_PROGRESS:
        raise HTTPException(status_code=400, detail="Task is already running")

    task.status = TaskStatus.IN_PROGRESS
    
    await update_task(settings.DATABASE_URL, task)
    task_runner = task_runner_factory(settings.DATABASE_URL, task.id)

    asyncio.create_task(task_runner())
    
    return task


@router.post("/{task_id}/cancel")
async def cancel_task(task_id: str) -> Task:
    task = await read_task(settings.DATABASE_URL, task_id)  
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if task.status not in [TaskStatus.IN_PROGRESS, TaskStatus.PAUSED]:
        raise HTTPException(status_code=400, detail="Task is not running or paused")

    task.status = TaskStatus.CANCELLED
    await update_task(settings.DATABASE_URL, task)
    return task


@router.post("/{task_id}/pause")
async def pause_task(task_id: str) -> Task:
    task = await read_task(settings.DATABASE_URL, task_id)   
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if task.status != TaskStatus.IN_PROGRESS:
        raise HTTPException(status_code=400, detail="Task is not running")
    
    task.status = TaskStatus.PAUSED
    await update_task(settings.DATABASE_URL, task)
    return task


@router.post("/{task_id}/resume")
async def resume_task(task_id: str) -> Task:
    task = await read_task(settings.DATABASE_URL, task_id) 
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if task.status != TaskStatus.PAUSED:
        raise HTTPException(status_code=400, detail="Task is not paused")
    task.status = TaskStatus.IN_PROGRESS
    await update_task(settings.DATABASE_URL, task)
    return task
