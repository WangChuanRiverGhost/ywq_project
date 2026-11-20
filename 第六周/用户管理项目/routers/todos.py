from fastapi import APIRouter
from schemas.todo import ToDo
router = APIRouter(prefix="/todos", tags=["待办"])

@router.post("/todos")
def create_todo(todo: ToDo):
    return {"message": "Todo created successfully"}

@router.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    return {"message": "Todo retrieved successfully"}

@router.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: ToDo):
    return {"message": "Todo updated successfully"}

@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    return {"message": "Todo deleted successfully"}