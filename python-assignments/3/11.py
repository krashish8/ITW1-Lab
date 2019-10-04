import random

with open("test.txt", "r") as f:
    l = len(f.readlines())
    i = random.randint(0,l)
    f.seek(0)
    print(f.readlines()[i])