# 周一：变量、数据类型、条件与循环

"""
一、变量
    本质是通过一个名称指向内存中被创建或已存在的数据，方便对其进行操作；
    变量在同一时间只能指向一个数据，多个变量可以指向同一数据。
    如：
        a = 111   同时在内存中创建a变量和111数据，并将a指向111
        b = a     在内存中创建b变量，并将其指向a变量指向的数据；此时a与b都指向111
        a = 222   在内存中创建222数据，并将a的指向改为222；此时a指向222，b指向111
二、数据类型
    指在python语言中可以被直接处理的数据类型。
    整数、浮点数、字符串、布尔值、空值
三、条件判断
    通过对不同条件的判断对数据做出不同的操作。
    if-elif-else
四、循环
    -for循环
        对有序的数据进行遍历。
        for-in
        range(a,b,c)函数：本质是创建一个range对象，当其被使用时，返回一个间隔为c，包含a，不包含b的整数列表；当a和c没有被赋值时，默认为0。
    -while循环
        符合条件时，不断进行while中的操作。
    -else子句
        for循环中，else将在for循环结束后执行；
        while循环中，else将在while后条件为False后执行；
        当循环中存在break时，优先执行break，即break的优先级高于else。
    -循环操作
        break：跳出最近一层循环；
        continue：终止本次循环，继续下一次循环；
        pass：占位符
五、match：对同一变量的不同值进行处理
    match-case
"""

# 练习一：数据类型与类型转换
name,age,height,is_student = "小明",18,1.75,True
student = [name,age,height,is_student]

for i in student:
    tp = type(i)
    print(f"当前数据：{i}\n该数据类型：{tp}\n————")

age = str(age)
print(type(age))
print(f"{name}今年{age}岁\n————————")

pai = "3.14"
print(type(pai))
pai = float(pai)
print(type(pai))
print(pai*2)

print("————————————")

# 练习二：条件判断
score = int(input("请输入分数："))
if score >= 90:
    level = "A"
elif 60 <= score <= 89:
    level = "B"
elif score <=59:
    level = "C"
print(f"您的分数：{score}\n您的等级：{level}")
# 思考题：用if语句判断当输入不是数字的情况；异常处理。
print("————————————")

# 练习三：循环
for i in range(1,101):
    if i%2 == 0:
        print(i)
print("————————")

num = 0
sum = 0
while sum <= 100:
    num += 1
    sum += num
    print(sum)
print(sum)
print("————————")

num = range(1,10)
list = []
for i in num:
    for b in num:
        if b > i:
            continue
        result = "【" + str(b) + "*" + str(i) + "=" + str(b*i) + "】"
        list.append(result)

    result_str = ""
    for r in list:
        result_str = result_str + r
    print(f"{result_str}\n")
    list.clear()
print("————————")

import random
num = random.randint(1,100)
user_num = int(input("请输入您本次的猜测："))
while user_num != num:
    if user_num > num:
        print("大了，请重新猜")
        user_num = int(input("请输入您本次的猜测："))
    elif user_num < num:
        print("小了，请重新猜")
        user_num = int(input("请输入您本次的猜测："))
else:
    print("恭喜")
print("————————————")

# 测试思维训练
"""
1、正常情况
    设程序生成50
    用户输入1-100内的数字时，当大于五十时输出“大了”；
    用户输入1-100内的数字时，当小于五十时输出“小了”；
    用户输入1-100内的数字时，当等于五十时输出“恭喜”，并游戏结束；
2、边界情况
    当用户输入0或101时，应该提示超出范围而不是直接报错
3、异常情况
    当用户输入非整数的情况下，应该提示输入整数
"""

# 面试题自测
"""
1、有五种，整数12，浮点数3.12，字符串"你好”，布尔值True、False，空值None
2、==是在比较两者的值是否相等，=是将=前的变量指向=后的变量所指向的内存中的数据，最终结果是=前后的变量同时指向内存中的同一个数据
3、break是直接终止循环，contiue是跳出本次循环，继续这层循环代码的下一次循环
4、让代码更易读
"""




