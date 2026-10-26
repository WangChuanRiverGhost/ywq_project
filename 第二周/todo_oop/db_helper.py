import sqlite3

class DBHelper:  # 创建一个数据库类，并对由其创建的实例赋予数据库连接conn和cursor

    def __init__(self,DB_PATH):

        self.conn = sqlite3.connect(DB_PATH)  # 数据库连接
        self.cursor = self.conn.cursor()  # 创建游标

        self.execute = self.cursor.execute  # sql语句

        self.commit = self.conn.commit  # 保存更改


    def db_cud(self,sql_text,*args):   # 创建表或增删改数据

        self.execute(sql_text,*args)

        self.commit()

        return True

    def db_r(self,sql_text,*args):  # 查数据

        self.execute(sql_text,*args)

        rows = self.cursor.fetchall()

        return rows

    def close_db(self):   # 关闭数据库连接

        self.conn.close()

        return True
