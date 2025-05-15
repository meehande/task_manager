import pytest
from fastapi.testclient import TestClient
from task_manager.routes.v1 import router, tasks
from task_manager.models import Task
from fastapi import HTTPException

client = TestClient(router)


@pytest.fixture
def example_task() -> Task:
    response = client.post(
        "/v1/tasks/", json={"title": "Test Task", "description": "Test Description"}
    )
    return Task(**response.json())


def test_create_task():
    response = client.post(
        "/v1/tasks/", json={"title": "Test Task", "description": "Test Description"}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"
    assert response.json()["description"] == "Test Description"


def test_get_task(example_task):
    response = client.get(f"/v1/tasks/{example_task.id}")
    assert response.status_code == 200
    assert response.json()["title"] == example_task.title
    assert response.json()["description"] == example_task.description


def test_run_task(example_task):
    response = client.post(f"/v1/tasks/{example_task.id}/run")
    assert response.status_code == 200
    assert response.json()["status"] == "in_progress"


def test_cancel_task_not_running(example_task):
    with pytest.raises(HTTPException):
        client.post(f"/v1/tasks/{example_task.id}/cancel")


def test_cancel_task(example_task):
    task_running = client.post(f"/v1/tasks/{example_task.id}/run")
    response = client.post(f"/v1/tasks/{example_task.id}/cancel")
    assert response.status_code == 200
    assert response.json()["status"] == "cancelled"


def test_pause_task_not_running(example_task):
    with pytest.raises(HTTPException):
        client.post(f"/v1/tasks/{example_task.id}/pause")


def test_pause_task(example_task):
    task_running = client.post(f"/v1/tasks/{example_task.id}/run")

    response = client.post(f"/v1/tasks/{example_task.id}/pause")
    assert response.status_code == 200
    assert response.json()["status"] == "paused"


def test_resume_task_not_running(example_task):
    with pytest.raises(HTTPException):
        client.post(f"/v1/tasks/{example_task.id}/resume")


def test_resume_task(example_task):
    task_running = client.post(f"/v1/tasks/{example_task.id}/run")
    task_paused = client.post(f"/v1/tasks/{example_task.id}/pause")
    response = client.post(f"/v1/tasks/{example_task.id}/resume")
    assert response.status_code == 200
    assert response.json()["status"] == "in_progress"
