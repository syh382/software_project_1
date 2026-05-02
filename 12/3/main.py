# 03
with open("information.text", "a") as t:
    while True:
        n = input()
        t.write(n + "\n")
        t.flush()
        print("작성됨.")


