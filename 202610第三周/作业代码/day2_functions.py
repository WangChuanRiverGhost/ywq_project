# 周二：函数、参数、作用域

# 练习一：基础函数
def add(a,b):
    return a + b
print(add(1,2))
print("————")
def is_even(n):
    if n%2 == 0:
        return "是偶数"
    else:
        return "不是偶数"
print(is_even(2))
print(is_even(1))
print("————")
def get_max(a,b,c):
    if a > b:
        d = a
    else:
        d = b
    if d > c:
        return d
    else:
        return c
print(get_max(33,44,55))
print("————")
def greet(name,greeting="你好"):
    print(f"{greeting},{name}")
    return True
greet("小明")
print("————————")

# 练习二：*args和**kwargs
def sum_all(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum
a = [1,2,3]
b = [10,20,30,40]
print(sum_all(*a))
print(sum_all(*b))
print("————")
def print_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} = {value}")
    return True
print_info(name="小明", age=18, city="北京")
print("————")
def process_data(a, b, *args, **kwargs):
    print(
        f"""
a：{a}
b：{b}
args：{args}
kwargs：{kwargs}
""")
    return True
process_data(1, 2, 3, 4, 5, name="test", x=100)
print("————————")

# 练习三：综合函数练习
def format_price(price, currency="¥"):
    price = f"{currency}{int(price)}"
    return price
print (format_price(100, currency="$"))
print("————")
def calc_bmi(height,weight):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        bmi_level = "偏瘦"
    elif bmi < 24:
        bmi_level = "正常"
    elif bmi <= 28:
        bmi_level = "偏胖"
    else:
        bmi_level = "肥胖"
    return bmi,bmi_level
print(calc_bmi(1.8,78))
print("————")
def build_url(host, port=80, path="/", **params):
    url = f"http://{host}:{port}{path}"
    num = 0
    for key,value in params.items():
        if num == 0:
            url += f"?{key}={value}"
            num += 1
        else:
            url += f"&{key}={value}"
    return url
print(build_url("example.com", port=8080, path="/api", q="python", page=1))
print("————————")
