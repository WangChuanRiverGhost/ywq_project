import time,functools

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
    print("你好")

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
@repeat(3)
def print_bye():
    print("bye")

print_hello()
ddel(1,2)    
print_bye()