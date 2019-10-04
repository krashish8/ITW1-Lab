with open('file1.txt') as f1:
    with open('file2.txt') as f2:
        for i, j in zip(f1.readlines(), f2.readlines()):
            print(i, end="")
            print(j, end="")