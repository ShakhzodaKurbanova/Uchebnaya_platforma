from sqlalchemy import (Column, String, Integer,
                        Float, DateTime, ForeignKey, Boolean)
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    phone_number = Column(String, unique=True)
    email = Column(String, unique=True)
    user_city = Column(String, nullable=True)
    birthday = Column(String, nullable=True)
    password = Column(String)
    reg_date = Column(DateTime, default=datetime.now())


class Course(Base):

    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    course_name = Column(String, nullable=True)
    reg_date = Column(DateTime, default=datetime.now())


class Task(Base):

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    task_name = Column(String, nullable=False)
    reg_date = Column(DateTime, default=datetime.now())


class Progress(Base):

    __tablename__ = "progress"

    id = Column(Integer, primary_key=True, autoincrement=True)


# async def create_tables():
#     async with engine.begin() as conn:
#         await conn.run_sync