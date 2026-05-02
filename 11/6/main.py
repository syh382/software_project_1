# 06
num = 1000
multiple1 = 2
multiple2 = 3

def func(num, multiple1, multiple2):
    s = 0
    for i in range(1, num + 1):
        if i % multiple1 == 0 or i % multiple2 == 0:
            s += i
    return s
print(func(num, multiple1, multiple2))




