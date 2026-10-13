# 周一：变量、数据类型、条件与循环

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
elif 60 <= score:
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




