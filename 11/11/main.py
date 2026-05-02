# 11
a = [35, 58, 69, 18, 84]
def average(num):
    aver = 0
    for i in num:
        aver += i
    aver = aver/len(num)
    return aver
print(average(a))

