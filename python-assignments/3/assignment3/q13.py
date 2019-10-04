with open('test.txt') as f:
    lines = f.readlines()
    words = []
    for i in lines:
        words.append(i.split())

print(words)