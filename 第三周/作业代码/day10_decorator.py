def fuc_name(func):
    def a():
        print(f"正在调用：{str(func.__name__)}")
        func()

@fuc_name
def print_func_name():
    print("你好")

@fuc_name
def print_happy():
    print("天天开心")

@fuc_name
def print_world():
    print("hello world")

try:
    print_world()
except TypeError as e:
    print(e)

def print_func_name_b():
    print(f"正在调用：{print_func_name_b.__name__}")
    print("你好")


def print_happy_b():
    print(f"正在调用：{print_happy_b.__name__}")
    print("天天开心")

def print_world_b():
    print(f"正在调用：{print_world_b.__name__}")
    print("hello world")

print("——————分隔线——————")
print_func_name_b()
print_happy_b()
print_world_b()
