# 04
for i in range(1,20):
    if i < 10:
        if i % 2 == 1:
            print(f"{"*"*i:^9}")
    else:
        if i % 2 == 1 and i > 11:
            print(f"{"*" * (20 - i):^9}")




