from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Todo(BaseModel):
    id: int
    title: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
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
