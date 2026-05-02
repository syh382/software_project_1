# 07
n = int(input("자연수 입력 "))
r = [0,1]
for i in range(2,n+1):
    r.append(r[i-1]+r[i-2])
print(sum(r))



