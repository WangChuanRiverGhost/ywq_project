import sqlite3

DB_PATH = "practice.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON;") 

"""建表"""
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY NOT NULL,
        name TEXT NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY NOT NULL,
        user_id INTEGER NOT NULL,
        amount REAL NOT NULL,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
""")

"""插入数据"""
name_list = [
    "张三",
    "李四",
    "王五",
    "赵六",
    "孙七"
]
for name in name_list:
    cursor.execute('INSERT INTO users("name") VALUES (?)',(name,))

order_list = [
    {"user_id": 1, "amount": 99.50},
    {"user_id": 2, "amount": 150.00},
    {"user_id": 1, "amount": 25.80},
    {"user_id": 9, "amount": 90.00},
    {"user_id": 4, "amount": 300.00}
]
for l in order_list:
    try:
        cursor.execute('INSERT INTO orders("user_id","amount") VALUES (?,?)',(l["user_id"],l["amount"]))
    except sqlite3.IntegrityError as e:
        print(f"本条数据插入失败，错误信息：{str(e)} 数据内容：{l}")
        continue
"""查询"""
cursor.execute('SELECT name,amount FROM users JOIN orders ON users.id = orders.user_id')
rows = cursor.fetchall()
print(f'1\n{rows}')

cursor.execute('SELECT name,amount FROM users LEFT JOIN orders ON users.id = orders.user_id')
rows = cursor.fetchall()
print(f'2\n{rows}')

cursor.execute('SELECT name, SUM(orders.amount) AS nums FROM users JOIN orders ON users.id = orders.user_id GROUP BY name')
rows = cursor.fetchall()
print(f'3\n{rows}')

cursor.execute('SELECT * FROM orders ORDER BY amount DESC')
rows = cursor.fetchall()
print(f'4\n{rows}')