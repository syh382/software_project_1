#8
h,r = map(int,input().split())
for i in range(r):
    for ii in range(2*h-1):
        if ii >= h:
            print(" " * (2*h-2-ii) + "*")
            continue
        print(" "*ii + "*")
