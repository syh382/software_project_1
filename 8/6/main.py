# 06
dict = {"이름":"송유현","나이":21,"학교":"전주대학교","학과":"컴퓨터공학과"}
while True:
    n = input("key입력: ")
    if n in dict:
        print(dict[n])
    else:
        print(n,"정보 없음")