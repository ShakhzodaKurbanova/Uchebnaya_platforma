from fastapi import FastAPI
from api.users.user_api import user_router
from api.courses.course_api import course_router
from api.tasks.task_api import task_router
from api.progress.progress_api import progress_router
from database import Base, engine

Base.metadata.create_all(engine)

app = FastAPI(docs_url="/")


app.include_router(user_router)
app.include_router(course_router)
app.include_router(task_router)
app.include_router(progress_router)