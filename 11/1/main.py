# 01
num1 = int(input("점수를 입력해주세요"))
num2 = int(input("점수를 입력해주세요"))
num3 = int(input("점수를 입력해주세요"))
def func(num1, num2, num3):
    max = 0
    for i in [num1, num2, num3]:
        if i > max:
            max = i
    return max
print(func(num1, num2, num3))

