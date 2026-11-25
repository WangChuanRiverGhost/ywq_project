import sqlite3

class DBHelper:  # 创建一个数据库类，并对由其创建的实例赋予数据库连接conn和cursor

    def __init__(self,DB_PATH):

        self.DB_PATH = DB_PATH  # 数据库路径

    def db_cud(self,sql_text,*args):   # 创建表或增删改数据

        with sqlite3.connect(self.DB_PATH) as conn:  # 新建连接
            conn.execute(sql_text, *args)

        return True

    def db_r(self,sql_text,*args):  # 查数据

        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.execute(sql_text, *args)
            rows = cursor.fetchall()

        return rows

    def close_db(self):   # 关闭数据库连接

        return True
