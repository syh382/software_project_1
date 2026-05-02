# 09
n = input()
def func(str):
    ex = []
    num = 1
    while len(ex) != len(n):
        ex.append(n[-num])
        num += 1
    print("".join(ex))
func(n)


