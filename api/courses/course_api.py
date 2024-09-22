from fastapi import HTTPException, APIRouter
from typing import List, Optional
from pydantic import BaseModel


course_router = APIRouter(prefix="/course", tags=["Courses API"])


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


courses = {} # Словарь для хранения курсов (временно, в реальном проекте используйте базу данных)


@course_router.post("/courses/create/")
async def create_course(course: Course):
    if course.name in courses:
        raise HTTPException(status_code=400, detail="Course with this name already exists")
    courses[course.name] = course
    return {"message": "Course created successfully"}


@course_router.get("/courses/")
async def get_courses():
    return list(courses.values())


@course_router.get("/courses/{course_id}")
async def get_course(course_id: str):
    if course_id not in courses:
        raise HTTPException(status_code=404, detail="Course not found")
    return courses[course_id]


@course_router.post("/courses/{course_id}/tasks/")
async def add_task_to_course(course_id: str, task: Task):
    if course_id not in courses:
        raise HTTPException(status_code=404, detail="Course not found")
    courses[course_id].tasks.append(task.name)
    return {"message": "Task added to course"}

# from fastapi import APIRouter
# from database.userservice import *
# from pydantic import BaseModel
# from api import result_message
# import re
#
#
# course_router = APIRouter(prefix="/course", tags=["Courses API"])
#
#
# class Course(BaseModel):
#     name: str
#     des: str
#     level: int
#     teacher: str
#     task: str
#
#
# @course_router.post("/register_user")
# async def register_user_api(user_data: User):
#     user_db = dict(user_data)
#     mail_validation = check_email(user_data.email)
#     if mail_validation:
#         result = register_user_db(**user_db)
#         return result_message(result)
#     return "Ошибка при заполнении почты"
#
#
# @user_router.post("/login_user")
# async def login_user_api(login: str, password: str):
#     result = login_user_db(login, password)
#     return result_message(result)
#
#
# @user_router.get("/get_profile_info")
# async def get_profile_api(user_id: int):
#     result = profile_info_db(user_id)
#     return result_message(result)
#
#
# @user_router.put("/change_profile")
# async def change_profile_api(user_id: int, change_info: str, new_info: str):
#     result = change_user_db(user_id, change_info, new_info)
#     return result_message(result)
#
#
# @user_router.delete("/delete_profile")
# async def delete_profile_api(user_id: int):
#     result = delete_user_db(user_id)
#     return result_message(result)
#
#
# @user_router.get("/get_all_users")
# async def get_all_users_api():
#     return get_all_users()