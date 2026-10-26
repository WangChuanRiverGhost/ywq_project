from manager import TaskManager

manager = TaskManager("todo.db","tasks")
manager.create_table("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY NOT NULL,
        title TEXT NOT NULL,
        status TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")
def test_add_task_increases_count():

    if not manager.get_all_tasks():
        before = 0
    else:
        before = len(manager.get_all_tasks())
    manager.add_task("买菜")
    after = len(manager.get_all_tasks())
    assert after == before + 1

def test_complete_task():
    l = ["吃饭","写作业","打游戏"]
    for i in l:
        manager.add_task(i)
    if not manager.get_tasks_by_status("已完成"):
        before = 0
    else:
        before = len(manager.get_tasks_by_status("已完成"))
    manager.complete_task(2)
    after = len(manager.get_tasks_by_status('已完成'))
    assert after == before + 1

def test_delete_task():
    before = len(manager.get_all_tasks())
    manager.delete_task(5)
    after = len(manager.get_all_tasks())
    assert after == before - 1



if __name__ == "__main__":
    test_add_task_increases_count()
    test_complete_task()
    test_delete_task()