from fastapi import APIRouter
from database.userservice import *
from pydantic import BaseModel
from api import result_message
import re


user_router = APIRouter(prefix="/user", tags=["Users API"])


regex = re.compile(r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$")


def check_email(email):
    if re.fullmatch(regex, email):
        return True
    return False


class User(BaseModel):
    name: str
    phone_number: str
    email: str
    password: str
    birthday: str
    user_city: str


@user_router.post("/register_user")
async def register_user_api(user_data: User):
    user_db = dict(user_data)
    mail_validation = check_email(user_data.email)
    if mail_validation:
        result = register_user_db(**user_db)
        return result_message(result)
    return "Ошибка при заполнении почты"

# @user_router.post("/register_user")
# async def register_user_api(name: str, phone_number: str, email: str,
#     password: str, birthday: str, user_city: str):
#     user_db = dict(User)
#     mail_validation = check_email(email)
#     if mail_validation:
#         result = register_user_db(**user_db)
#         return result_message(result)
#     return "Ошибка при заполнении почты"


@user_router.post("/login_user")
async def login_user_api(login: str, password: str):
    result = login_user_db(login, password)
    return result_message(result)


@user_router.get("/get_profile_info")
async def get_profile_api(user_id: int):
    result = profile_info_db(user_id)
    return result_message(result)


@user_router.put("/change_profile")
async def change_profile_api(user_id: int, change_info: str, new_info: str):
    result = change_user_db(user_id, change_info, new_info)
    return result_message(result)


@user_router.delete("/delete_profile")
async def delete_profile_api(user_id: int):
    result = delete_user_db(user_id)
    return result_message(result)


@user_router.get("/get_all_users")
async def get_all_users_api():
    return get_all_users()