import sqlite3

DB_NAME = "todo.db"   # 库名
DB_PATH = f"第一周/todo_project/{DB_NAME}"   # 数据库路径

# 连接数据库，创建游标
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

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
            cerated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
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

    return rows 

def get_tasks_by_status(status):   # 按状态筛选任务

    cursor.execute("SELECT id,title,cerated_at FROM tasks where status = ?",(status,))
    rows = cursor.fetchall()

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

