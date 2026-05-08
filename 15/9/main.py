#9
import sys
args = sys.argv
with open(f"{args[1]}", "r",encoding = 'utf-8') as f:
    c = f.read()
with open(f"{args[2]}", "w",encoding = 'utf-8') as f:
    f.write(c)