# 06
b = [[],[]]
with open("info.txt", "r",encoding = 'utf-8') as a:
    b[0] = a.readline().split(",")
    b[1] = a.readline().split(",")
def sum_average(name,*numbers):
    with open("result.txt","a",encoding = 'utf-8') as f:
        f.write(f"이름 {name}, 총점 {sum(numbers)}, 평균 {sum(numbers)/len(numbers)}\n")
        if sum(numbers)/len(numbers) >= 60:
            f.write("합격\n")
        else:
            f.write("불합격\n")
sum_average(b[0][0],int(b[0][1]),int(b[0][2]),int(b[0][3]))
sum_average(b[1][0],int(b[1][1]),int(b[1][2]),int(b[1][3]))
