from fastapi import APIRouter,Depends

from schemas.todo import ToDo  # 导入todo的pydantic模型（用于用户输入检测）
from service.db_operation.manager import TaskManager  # 导入代办具体增删改查的类

router = APIRouter(prefix="/todos", tags=["待办"])


DB_PATH = "todo.db"  # 数据库路径
TABLE_NAME = "todo_list"  # 代办表表名

def get_manager():
    return TaskManager(DB_PATH, TABLE_NAME)

"""增加代办"""
@router.post("/create-todo")  # 新增代办
def create_todo(todo: ToDo,manager:TaskManager = Depends(get_manager)):
    manager.add_task(title=todo.title)
    return {"message": f"代办已添加 标题：{todo.title}"}

"""查询代办"""
@router.get("/check-todo")  # 查询所有任务
def get_todo(manager:TaskManager = Depends(get_manager)):
    rows = manager.get_all_tasks()
    return {"message": rows}

@router.get("/check-todo/not-finished")  # 查询未完成任务
def get_not_finished_todo(manager:TaskManager = Depends(get_manager)):
    rows = manager.get_tasks_by_status("未完成")
    return {"message": rows}

@router.get("/check-todo/finished")  # 查询已完成任务
def get_finished_todo(manager:TaskManager = Depends(get_manager)):
    rows = manager.get_tasks_by_status("已完成")
    return {"message": rows}

"""修改代办"""
@router.put("/edit-todo/{todo_id}")  # 修改代办状态
def update_todo(todo_id: int,manager:TaskManager = Depends(get_manager)):
    manager.complete_task(todo_id)
    return {"message": "状态修改完成"}

"""删除代办"""
@router.delete("/delete-todo/{todo_id}")  # 删除代办
def delete_todo(todo_id: int,manager:TaskManager = Depends(get_manager)):
    manager.delete_task(todo_id)
    return {"message": "代办已删除"}