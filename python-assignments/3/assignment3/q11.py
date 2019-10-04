import random

with open('test.txt') as f:
    lines = f.readlines()
    print(lines[random.randrange(len(lines))], end="")