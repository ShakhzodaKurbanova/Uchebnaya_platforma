from fastapi import APIRouter, HTTPException
from typing import List, Optional
from pydantic import BaseModel

progress_router = APIRouter(prefix="/progress", tags=["Progress API"])

# ... (модели данных Course, Task, ... из предыдущего кода)

progress = {}  # Словарь для хранения данных о прогрессе пользователей (временное решение)


class Progress(BaseModel):
    course_id: str
    user_id: str
    completed_tasks: List[str] = []  # Список идентификаторов выполненных заданий
    total_points: int = 0
    percentage_completed: float = 0.0


@progress_router.get("/progress/{user_id}/{course_id}/")
async def get_user_progress(user_id: str, course_id: str):
    if course_id not in progress:
        raise HTTPException(status_code=404, detail="Course not found")
    if user_id not in progress[course_id]:
        raise HTTPException(status_code=404, detail="User progress not found")
    return progress[course_id][user_id]

# ... (остальные endpoint'ы)
