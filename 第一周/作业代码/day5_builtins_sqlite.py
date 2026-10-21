# 周五：内置函数、字符串处理、SQLite入门

# 练习一：内置函数
print("练习一：内置函数")
num = ["1","2","3"]
print(f"1、{list(map(int,num))}")
def is_posnum(num):
    if num > 0:
        return True
    else:
        return False
num = [-1, 0, 3, -5, 8]
print(f"2、{list(filter(is_posnum,num))}")
ls = ["苹果","香蕉","橘子"]
st = ""
for key,value in enumerate(ls,start=0):
    st += f"，{key}:{value}"
print(f"3、{st.replace("，","",1)}")
names=["a","b"]
ages=[1,2]
print(f"4、{dict(zip(names,ages))}")
print(f"5、{list(sorted(["banana","apple","cherry"],key=len))}")
print(f"6、{any(x % 2 == 0 for x in [1, 3, 5, 6])}")
print(f"7、{all(x % 2 == 0 for x in [1, 2, -3, 4])}")

# 练习二：字符串处理
print("练习二：字符串处理")
print(f"1、{"hello world".title()}")
a,b,c = "2026-10-16".split(sep="-")
print(f"2、a={a},b={b},c={c}")
x = "name=小明&age=18&city=北京".split("&")
y = {}
for i in x:
    a = i.split("=")
    y[a[0]] = a[1]
print(f"3、{y}")
print(f"4、{" ".join(["Python", "is", "awesome"])}")
def format_phone(phone):
        return f"{phone[:3]}-{phone[3:7]}-{phone[7:]}"
print(f"5、{format_phone("13812345678")}")

# 练习三：SQLite操作
print("练习三：SQLite操作")
import sqlite3
conn = sqlite3.connect("practice.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY NOT NULL,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        price INTEGER NOT NULL
    )
""")
book = [("Python入门","张三",59.9), ("FastAPI实战","李四",79.9), ("SQLite指南","王五",39.9)]
for i in book:
    cursor.execute("INSERT INTO books (title,author,price) VALUES (?, ?, ?)",i)
cursor.execute("SELECT * FROM books")
rows = cursor.fetchall()
for row in rows:
    print(row)
x = cursor.execute("SELECT title FROM books where price>50")
print(list(x))
cursor.execute("UPDATE books SET price=? WHERE title=?",(49.0,"Python入门"))
cursor.execute("DELETE FROM books WHERE title=?",("SQLite指南",))

conn.commit()
conn.close()