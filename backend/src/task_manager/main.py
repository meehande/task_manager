from fastapi import FastAPI, HTTPException
from task_manager.routes.v1 import router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(
    title="Task Manager API",
    description="A task management system for Frontier Health Application",
    version="0.1.0",
)


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)


@app.get("/")
async def root():
    return "Task Manager API is running! Please use the /docs endpoint to view the API documentation."


@app.get("/_healthcheck", include_in_schema=False)
async def healthcheck():
    return {"status": "ok"}


def main():
    uvicorn.run(
        "task_manager.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )


if __name__ == "__main__":
    main()
