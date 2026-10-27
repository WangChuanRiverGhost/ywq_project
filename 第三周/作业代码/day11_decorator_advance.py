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
    def y(a,b):
        num = func(a,b)
        print(f"返回值：{num}")
    return y
@log
def add(a,b):
    print(f"函数名：{add.__name__} 函数参数：{a},{b}")
    return a + b

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
add(1,2)    
print_bye()