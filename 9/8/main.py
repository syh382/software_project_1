# 08
n = []
while True:
    ex = int(input())
    if ex == 0:
        print(sum(n), sum(n)/len(n))
        break
    else:
        n.append(ex)

