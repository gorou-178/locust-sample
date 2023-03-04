import time

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from starlette import status

app = FastAPI()


class Todo(BaseModel):
    id: int
    title: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    if todo_id % 5 == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Article with id {id} not found"
        )
    return {
        "todo": {
            "id": todo_id,
            "title": f"test_{todo_id}"
        }
    }


@app.post("/todos")
def create_todo(todo: Todo):
    return {
        "id": todo.id,
        "title": todo.title
    }
