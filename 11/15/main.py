# 15
n = int(input())
def number(n):
    a = []
    for i in range(n):
        a.append(str(i+1))
    for i in range(n):
        for ii in range(1,n+1):
            print(ii+i, end="")
        print('')
    for i in range(n-1,-1,-1):
        print(f"{"".join(a[i:]):>{n}}")
    a = []
    b = 1
    for i in range(n):
        if i >= 1:
            for ii in range(i+1, i+3):
                b += 1
                a.append(str(b))
        else: a.append(str(b))
        print("".join(a[i:]))
number(n)
