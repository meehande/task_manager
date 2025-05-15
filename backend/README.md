# Task Manager Backend

A FastAPI-based backend service for managing long-running tasks.

## Running locally

This project uses `uv` for dependency management. To set up the development environment:

Create a virtual environment and install dependencies:
```bash
uv sync
```

To run the development server:
```bash
cd backend
uv run -m task_manager.main   
```

The API will be available at http://localhost:8000


To run unit tests:
```bash
uv run python -m pytest ./tests
```


## Deployment

Build a docker image
```bash
cd backend 
docker build -f ./deployment/Dockerfile . -t task-manager-backend:latest
```

To run the docker image:
```bash
docker run -p 8000:8000 task-manager-backend:latest
# Exposes docs on: http://localhost:8000/docs
```

This can be pushed to a container registry for deployment.