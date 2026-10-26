from db_helper import DBHelper

class TaskManager:

    def __init__(self,DB_PATH,table_name):

        self.db = DBHelper(DB_PATH)
        self.tablename = table_name

    def create_table(self,sql_text):

        self.db.db_cud(sql_text)

        return True
  
    def add_task(self,title):   # 添加任务

        self.db.db_cud(f"INSERT INTO {self.tablename} (title,status) VALUES (?,?)",(title,"未完成"))

        return True

    def get_all_tasks(self):   # 获取所有任务

        rows = self.db.db_r(f"SELECT * FROM {self.tablename}")

        if not rows:
            return False
        
        return rows

    def get_tasks_by_status(self,status):   # 按状态筛选任务

        rows = self.db.db_r(f"SELECT id,title,status,created_at FROM {self.tablename} where status = ?",(status,))

        if rows == []:
            return False
        
        return rows

    def complete_task(self,task_id):   # 标记任务完成

        self.db.db_cud(f"UPDATE {self.tablename} SET status = '已完成' WHERE id = ?",(task_id,))

        return True

    def delete_task(self,task_id):   # 删除任务

        self.db.db_cud(f"DELETE FROM {self.tablename} WHERE id = ?",(task_id,))

        return True

    def check_error(self,i):   # 检测用户选择是否存在于数据库
        rows = self.get_all_tasks()
        
        for row in rows:
            if i != row[0]:
                continue
            else:
                return False
            
        return True
        
