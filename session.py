from fastapi import Request,Depends
from typing import Annotated
from sqlmodel import Session
def get_session_reuse(request:Request):
    db = request.app.state.db_init
    yield from db.get_session()

SessionDep = Annotated[Session,Depends(get_session_reuse)]