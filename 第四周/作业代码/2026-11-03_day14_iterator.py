import time
class Countdown:
    def __init__(self,c_second):
        self.c_second = c_second
    def __iter__(self):
        print(self.c_second)
        return self

    def __next__(self):
        time.sleep(1)
        if self.c_second >= 1:
            self.c_second -= 1
            n_second = self.c_second
            return n_second
        
        else:
            raise StopIteration

cs = iter(Countdown(3))
for i in range(3):
    print(next(cs))

print(next(cs))
print(next(cs))
print(next(cs))
