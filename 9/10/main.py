# 10
n = list(input())
ex = []
l = 1
while True:
    ex.append(n[-l])
    l+=1
    if l > len(n):
        print("".join(ex))
        break


