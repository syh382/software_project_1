# 03
#90점 이상 A, 80점 이상 B, 70점 이상 C, 60점 이상 D, 그 외 F
n = int(input("점수 입력"))
def func(num):
    if num >=90:
        result = "A"
    elif num >=80:
        result = "B"
    elif num >=70:
        result = "C"
    elif num >=60:
        result = "D"
    else:
        result = "F"
    return result
print(func(n))


