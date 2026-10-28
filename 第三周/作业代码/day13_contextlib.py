from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.time()
    try:
        yield start
    except:
        print("错误")
    finally:
        end = time.time()
        print(f"总用时：{end-start}")
with timer():
    print("aa")

@contextmanager
def managedfile(path):
    file = open(path)
    try:
        yield file
    except:
        print("错误")
    finally:
        file.close()        

with managedfile("第三周/作业代码/aaa.txt") as f:
    content = f.read()
    print(content)