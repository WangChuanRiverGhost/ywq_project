import time,functools,inspect

def timer(func):
    @functools.wraps(func)
    def x():
        start = time.time()
        func()
        end = time.time()
        print(f"执行花了{end-start}秒")
    
    return x

@timer
def print_hello():
    for i in range(1,10):
        print(i,"你好")

def log(func):
    @functools.wraps(func)
    def y(*args):
        print(f"函数名：{func.__name__}\函数参数：{inspect.signature(func)}")
        num = func(*args)
        print(f"返回值：{num}")
    return y

@log
def ddel(a,b):
    return a - b


def repeat(n):
    def z(func):
        @functools.wraps(func)
        def a():
            for i in range(n):
                func()
        return a
    return z
@repeat(5)
def print_bye():
    print("拜拜")

print_hello()
ddel(3,4)
print_bye()

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self.start

    def __exit__(self, exc_type, exc, tb):
        end = time.time()
        print(f"总用时：{end-self.start}")
        return True
with Timer() as i:
    print("hello")

class ManagedFile:

    def __init__(self,path):
        self.path = path
    def __enter__(self):
        self.file = open(self.path)
        return self.file

    def __exit__(self, exc_type, exc, tb):
        self.file.close()
        return False

with ManagedFile("第三周/作业代码/aaa.txt") as f:
    content = f.read()
    print(content)