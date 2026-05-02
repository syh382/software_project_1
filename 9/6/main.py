# 06
n = 0
for i in range(1, 1001):
    if i % 2 == 0 or i % 3 == 0:
        n += i
print(n)