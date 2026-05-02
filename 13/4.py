# 04
n = int(input())
for i in range(n-2):
    if i == 0 or i == n-1:
        print("*"*n)
        continue
    print("*" + " " * (n-2) + "*")





