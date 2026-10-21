# 周三：类与对象入门

class Person:

    def __init__(self,name,age,weight,height):
        
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def greet(self):
        pass

    def calc_bmi(self):
        self.bmi = self.weight / (self.height ** 2)
        if self.bmi < 18.5:
            self.bmi_level = "偏瘦"
        elif self.bmi < 24:
            self.bmi_level = "正常"
        elif self.bmi <= 28:
            self.bmi_level = "偏胖"
        else:
            self.bmi_level = "肥胖"

        return self.bmi,self.bmi_level

class Student:

    def __init__(self,scores):
        
        self.scores = scores

    def get_average(self):

        score = sum(self.scores) / 5

        return score

lili = Student([85, 90, 78, 92, 88])
print(lili.get_average())

print("""
4、Person.species是类属性，p1.species是实例属性。
当前者被查找时，优先查找类属性，其次为父级属性；
当后者被查找时，优先查找实例属性，实例属性不存在时，查找其所在的类属性，最后是父级属性。
""")

# 原代码
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

kiki = Person("kiki",18,65,1.75)
print(kiki.calc_bmi())