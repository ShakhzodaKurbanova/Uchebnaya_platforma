from fastapi import APIRouter, HTTPException
from typing import List, Optional
from pydantic import BaseModel


task_router = APIRouter(prefix="/task", tags=["Tasks API"])


class Course(BaseModel):
    name: str
    description: str
    level: str
    teacher: str
    tasks: List[str] = [] # Список идентификаторов заданий, связанных с курсом


class Task(BaseModel):
    name: str
    description: str
    type: str
    points: int
    status: str


tasks = {} # Словарь для хранения заданий (временное решение, в реальном проекте используйте БД)


@task_router.get("/tasks/{task_id}/")
async def get_task(task_id: str):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]


@task_router.post("/tasks/{task_id}/submit/")
async def submit_task(task_id: str, solution: str):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    # Проверка решения (в реальном проекте может быть сложная логика проверки)
    # ...

    # Сохранение решения (в реальном проекте записывается в БД)
    # ...

    # Обновление статуса задания
    tasks[task_id].status = "submitted"
    return {"message": "Task submitted successfully"}

# ... (остальные endpoint'ы)
