# 13
num = 5
def dia(num):
    for i in range(1,2*num):
        if i % 2 == 1:
            print(f"{"*"*i:^{2*num-1}}")
    for i in range(1, 2*num):
        if i % 2 == 1:
            print(f"{"*"*(10-i):^{2*num-1}}")
dia(num)