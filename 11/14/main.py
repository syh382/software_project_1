# 14
num = int(input())
def star(n):
    for i in range(1, n + 1):
        print(f"{"*" * i:>{n}}")
    print("")
    for i in range(1, n * 2):
        if i > n:
            print(f"{"*" * (n * 2 - i):{n}}", end="")
            print(f"{"*" * (n * 2 - i):>{n}}")
        else:
            print(f"{"*" * i:{n}}", end="")
            print(f"{"*" * i:>{n}}")
    print("")
    for i in range(1, 2 * n - 1):
        if i == 1:
            print(f"{"*":^{2 * n - 1}}")
        elif i % 2 == 1:
            print(f"{"*" + " " * (i - 2) + "*":^{2 * n - 1}}")
    print("*" * (2 * n - 1))


star(num)