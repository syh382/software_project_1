# 12
a = [51, 9, 48, 76, 25]
def m(num):
    n = 0
    for i in num:
        if i > n:
            n = i
    return n
print(m(a))