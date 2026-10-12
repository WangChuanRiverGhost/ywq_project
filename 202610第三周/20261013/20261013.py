# 周二：函数、参数、作用域

"""
一、函数
    通过创建函数对象的方式对某一通用过程进行抽象。
    调用函数：通过 函数名() 的方式调用函数，其中，函数名是内存中一个函数对象的引用，将其用变量指向时，可以通过该变量访问该函数。
    定义函数：通过def进行函数定义，通过return返回函数运行后的值。
    递归函数：可以在函数中调用它本身。
二、函数参数
    -位置参数
        定义有位置参数的函数后，调用该函数时按照位置参数顺序传入即可按序填入函数的位置参数中。
    -默认参数
        定义有默认参数的函数时，在参数后加入=为其赋值。当该参数没有被传入其他值时，该参数的值为=后面的值。需要注意的是，该值应当为一个不变对象。
    当传入的参数数量不定时，可使用以下两种参数：
    -可变参数
        def func(*args)
        定义有可变参数的函数时，在参数前加*表示其为可变参数。
        调用存在可变参数的函数时，应在可变参数的位置传入一个元组或列表；调用后，将根据该元组/列表转化为一个元组。
        当传入的是一个指向列表/元组的变量时，应当在该变量前加*。
    --关键字参数
        def func(**kwargs)
        定义有关键字参数的函数时，在参数前加**表示其为关键字参数。
        调用存在关键字参数的函数时，应在关键字参数的位置传入一个字典；调用后，将根据该字典生成一个other:{}的键值对。
        当传入的是一个指向字典的变量时，应当在该变量前加**。
    当传入的关键字参数固定时，可以使用以下参数：
    --命名关键字参数
        def func(*,)
        定义有命名关键字参数的函数时，与其他参数之间用*,隔开。*后的参数无需额外定义。
        其他属性同关键字参数。
    当参数中同时存在以上不同类型的参数时，应按照从上至下的顺序安排参数位置。
三、作用域
    LEGB：L（函数内部）；E（包含该函数的外部函数）；G（当前py文件）；B（python的内置语言）
    访问该数据的范围；当查找数据时，按照LEGB的顺序进行查找。
"""

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
def format_price(price, currency="¥", decimals=2):
    price = f"{currency}{int(price)}"
    return price
print (format_price(100, currency="$", decimals=0))
print("————")
def calc_bmi(height,weight):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        bmi_level = "偏瘦"
    elif 18.5 <= bmi < 24:
        bmi_level = "正常"
    elif 24 <= bmi <= 28:
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

# 测试思维训练
"""
1、正常情况：
    当身高体重计算结果符合范围内，显示bmi及其等级
2、边界情况
    bmi在边界时显示问题
3、异常情况
    输入不符合规定时（如单位不符合，输入非数字时）异常提醒
"""

# 面试题自测
"""
1、*args传入元组/列表，在函数内部自动转化为元组；**kwargs传入字典，在函数内部自动转化为字典
2、默认参数需要是不可变的数据，或在函数内部使其为空。否则可能会出现存在调用残留数据的情况。
3、元组
4、局部变量出该局部作用域后不可用；在调用时python优先寻找局部变量。当需要在局部作用域中用到全局变量时，用global声明。
"""