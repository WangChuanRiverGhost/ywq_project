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




