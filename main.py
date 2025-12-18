from fastapi import FastAPI 
from contextlib import asynccontextmanager
from db import DBConfig
from TodoModel import Todo
from todo_router import router as TodoRouter
@asynccontextmanager
async def lifespan(app:FastAPI):
    database = DBConfig(url="your url")
    database.openConnection()
    database.create_tables()
    app.state.db_init = database
    yield
    database.closeConnection()

app = FastAPI(lifespan=lifespan)

app.include_router(TodoRouter)