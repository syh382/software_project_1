# 08
n = int(input())
for i in range(1,2*n):
    if  i % 2 == 1:
        print(f"{"*"*(2*n-i):^{2*n-1}}")
for i in range(1,2*n):
    if i % 2 == 1 and i > 1:
        print(f"{"*"*i:^{2*n-1}}")
