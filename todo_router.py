from fastapi import APIRouter, HTTPException
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
    existing_todo = session.exec(select(Todo).where(Todo.content == todo.content)).first()
    if existing_todo:
        raise HTTPException(status_code=400, detail=f"Content: {todo.content} already exists!")

    db_todo = Todo.model_validate(todo)
    print(db_todo)
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo


@router.get("/todos/{todo_id}")
def read_todo(todo_id: int, session: SessionDep) -> Todo:
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

    

@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, session: SessionDep):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    session.delete(todo)
    session.commit()
    return {"detail":"Todo deleted!"}