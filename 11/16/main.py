# 16
num = 1000
def dia(num):
    result = 0
    n = 0
    while result < num:
        n += 1
        result = n ** 2
    print(n, result)
dia(num)