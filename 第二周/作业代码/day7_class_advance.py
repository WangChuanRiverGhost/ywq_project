class Animal:
    def __init__(self,name):
        self.name = name

    def go(self):
        print("Animal 运行")
        return True

class Dog(Animal):
    def go(self):
        print("Dog 运行")
        return True

class Cat(Animal):
    def go(self):
        print("Cat 运行")
        return True

jinmao = Dog("金毛")
zheerma = Cat("折耳猫")

print(jinmao.name,zheerma.name)
print(jinmao.go(),zheerma.go())

class BankAccount:
    def __str__(self):
        return f"当前余额：{self.__balance}"

    def __repr__(self):
        return f"{self}：{self.__balance}"
    
    def __init__(self,initial_balance):
        self.__balance = initial_balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("存款金额必须大于0，请重新操作")
            return False
        return True

    def withdraw(self,amount):
        if amount <= 0:
            print("取款金额必须大于0，请重新操作")
            return False

        try:
            if self.__balance > amount:
                self.__balance -= amount
            else:
                raise ValueError("余额不足")
        except ValueError:
            print("余额不足，请充值后重试")
            return False
        return True

my_zh = BankAccount(1000)
print(my_zh)
print([my_zh])
