from fastapi import APIRouter
from session import SessionDep
from sqlmodel import select
from TodoModel import TodoCreate,Todo
router = APIRouter(prefix="/api")

@router.get('/todos/')
def read_todos(session:SessionDep)->list[Todo]:
    todos = session.exec(select(Todo)).all()
    return todos

@router.post('/todos/')
def create_todo(todo:TodoCreate,session:SessionDep)->Todo:
    db_todo = Todo.model_validate(todo)
    print(db_todo)
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo

    

