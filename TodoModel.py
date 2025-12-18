from sqlmodel import SQLModel,Field

class TodoCreate(SQLModel):
    content:str = Field(index=True,unique=True,min_length=1,max_length=10)


class Todo(SQLModel,table = True):
    id:int=Field(default=None,primary_key=True)
    content:str = Field(index=True,unique=True,min_length=1,max_length=10)