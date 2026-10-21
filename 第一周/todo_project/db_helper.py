import sqlite3

DB_NAME = "todo.db"   # 库名
DB_PATH = f"第一周/todo_project/{DB_NAME}"   # 数据库路径

# 连接数据库，创建游标
conn = None
cursor = None

def init_db():   # 初始化数据库，创建表
    global conn,cursor
    # 连接数据库，创建游标
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 创建表
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY NOT NULL,
            title TEXT NOT NULL,
            status TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # 提交修改
    conn.commit()

    return True

def add_task(title):   # 添加任务

    cursor.execute("INSERT INTO tasks (title,status) VALUES (?,?)",(title,"未完成"))
    conn.commit()
    return True

def get_all_tasks():   # 获取所有任务

    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()

    if not rows:
        return False
    
    return rows 

def get_tasks_by_status(status):   # 按状态筛选任务

    cursor.execute("SELECT id,title,status,created_at FROM tasks where status = ?",(status,))
    rows = cursor.fetchall()

    if rows == []:
        return False
    
    return rows

def complete_task(task_id):   # 标记任务完成

    cursor.execute("UPDATE tasks SET status = '已完成' WHERE id = ?",(task_id,))
    conn.commit()

    return True

def delete_task(task_id):   # 删除任务

    cursor.execute("DELETE FROM tasks WHERE id = ?",(task_id,))
    conn.commit()

    return True

def close_db():   # 关闭数据库连接

    conn.close()

    return True

def check_error(i):   # 检测用户选择是否存在于数据库
    rows = get_all_tasks()
    
    for row in rows:
        if i != row[0]:
            continue
        else:
            return False
    return True
    
