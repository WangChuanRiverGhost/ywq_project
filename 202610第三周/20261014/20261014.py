# 周三：异常处理

# 练习一：基础异常捕获
def int_num():
    while True:
        try:
            num = input("请输入一个数字：")
            int_n = int(num)
            print(f"数字：{int_n}|数据类型：{type(int_n)}")
            return True
        except ValueError:
            print("请输入有效数字")
            continue
        finally:
            pass
int_num()
print("————")
def safe_divide(a,b):
    try:
        c = a/b
        return c
    except ZeroDivisionError:
        print("除数不能为0")
        return True
    except TypeError:
        print("请输入数字")
    finally:
        pass
safe_divide("a",0)
safe_divide("a",0)
num = safe_divide(2,3)
print(num)
print("————")
def get_element(lst,index):
    try:
        s = lst[index]
        return s
    except IndexError:
        return None
    finally:
        pass
print(get_element([1,2],1))
print("————————")

# 练习二：raise与自定义异常
def check_age(age):
    if age < 0:
        raise ValueError("年龄不能为负数")
    elif age > 150:
        raise ValueError("年龄不合理")
    else:
        return age
def check_password(password):
    if len(password) < 6:
        raise ValueError("密码太短")
    elif len(password) > 20:
        raise ValueError("密码太长")
    else:
        num = 0
        for p in password:
            try:
                int(p)
                num += 1
            except ValueError:
                continue
        if num == 0:
            raise ValueError("密码需要包含数字")
        else:
            return("密码合法")
try:
    check_age(160)
except ValueError as e:
    if str(e) == "年龄不能为负数":
        print("年龄不能为负数，请重新输入")
    else:
        print("年龄不合理，请重新输入")
try:
    check_password("111")
except ValueError as e:
    if str(e) == "密码太短":
        print("密码应大于六位数，请重新输入")
    elif str(e) == "密码太长":
        print("密码应小于20位，请重新输入")
    else:
        print("密码需要包含数字，请重新输入")
print("————————")

# 综合练习：改造猜数字游戏
import random

num = random.randint(1,100)
input(
    """
这是一个猜数字游戏。
系统将随机生成一个1-100（包含1和100）的数字。
如果你在十回合内猜到了答案，恭喜你胜利了。
【按回车开始游戏】"""
)
fre = 0
while True:
    try:
        user_num = int(input("请输入您本次的猜测："))
        if not 1 <= user_num <= 100:
            raise ValueError("数字超出范围")
        elif user_num > num:
            fre += 1
            print(f"当前轮次：{fre}")
            if fre == 10:
                break
            print("大了，请重新猜")
            continue
        elif user_num < num:
            fre += 1
            print(f"当前轮次：{fre}")
            if fre == 10:
                break
            print("小了，请重新猜")
            continue
        else:
            fre += 1
            print(f"恭喜你赢了！共用轮次：{fre}")
            break
    except ValueError as e:
        mes = str(e)
        if "invalid literal" in mes: 
            print("请输入数字")
        else:
            print("数字超出范围，请重新输入")
        continue
    finally:
        if fre == 10:
            print("次数用完，游戏结束")

# 测试思维训练
"""
1、正常情况
    密码包含数字且密码的字符串长度在6-20（包含边界值）之间：输入abc1234，返回'密码合法'
2、边界情况
    密码长度六位：输入abc123，返回'密码合法'；
    密码长度二十位：输入1234567890qwertyuiop，返回'密码合法'；
    密码长度五位：输入abc12，返回'密码应大于六位数';
    密码长度二十一位：输入1234567890qwertyuiopa，返回'密码长度应小于20位数'
3、异常情况
    密码是空字符串：提示'请输入密码'；
    密码不包含数字：qwertyui提示'请输入含有数字的密码'；
    密码长度不符合但包含数字：qw12提示'密码应大于六位数'或'密码应小于二十位数'；
    密码长度不符合且不包含数字：qwer结合以上两者提示；
    密码是中文字符：提示'请输入英文字母和数字作为您的密码'
"""

# 面试题自测
"""
1、优先执行try，当try中的错误被成功捕获，可以通过except对其捕获的错误情况进行处理；当try中没有出现问题，执行else；无论try有没有错误被捕获，在except或者else后执行finally。
2、具体的错误信息
3、当一些错误不在程序可识别的范畴内时用raise，如计算bmi值，如果传入数据为负数，在程序里是可以跑通算出来一个负数结果的，并且不会报错，但是我们期望最终呈现的bmi值这个结果不为负数，此时可以用raise；
   当我们期望对错误信息进行处理而不是让程序直接报错时使用except。
4、执行在这个代码块中无论是否报错都进行下去的程序
"""
            
