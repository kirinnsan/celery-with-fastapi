from typing import Optional

from worker import celery
from fastapi import Body, FastAPI, Request
from pydantic import BaseModel

from worker import create_task


app = FastAPI()


class TaskAPISchemaIn(BaseModel):
    wait: int


class TaskAPISchemaOut(BaseModel):
    task_id: str
    task_status: Optional[str]
    task_result: Optional[bool]


@app.get("/")
def root():
    return {"message": "FastAPI Celery Test"}


@app.post("/tasks", status_code=201)
def run_task(payload: TaskAPISchemaIn):
    task = create_task.delay(payload.wait)
    return {"task_id": task.id}


@app.get("/tasks/{task_id}")
def get_status(task_id: str):
    task_result = celery.AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return TaskAPISchemaOut(**result)
