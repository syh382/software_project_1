# 07
with open("args.txt","r") as f:
    args = f.readline().split()
    print(args)
    mi,ma = input().split()
def a(args,ma,mi):
    lis=[]
    for i in args:
        if int(i) <= int(ma) and int(i) >= int(mi):
            lis.append(int(i))
    return lis
print(a(args,ma,mi))





