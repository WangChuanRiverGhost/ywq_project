import time
def read_large_file(path):
    with open(path,'r',encoding='utf-8') as f:
        for line in f:
            yield line.split(sep="\n")[0]

read_finally = False
path = "第四周/day14_作业代码测试文件.txt"
line = read_large_file(path)

while not read_finally:
    try:
        time.sleep(1)
        print(next(line))
    except StopIteration:
        read_finally = True
    finally:
        pass

with open(path, "r", encoding="utf-8") as f:
    file_text = f.readlines()
print(file_text)


           
def fib(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a,b = b,a + b

x = fib(5)
for i in range(5):
    print(next(x))


