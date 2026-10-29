def make_counter():

    num = 0
    def count():

        nonlocal num

        print(num)

        num += 1

    return count

def make_power(n):
    def power(x):
        return x ** n

    return power

c = make_counter()
print("【1、")
for i in range(5):
    c()
print("【2、")
p = make_power(3)
print(p(2))


