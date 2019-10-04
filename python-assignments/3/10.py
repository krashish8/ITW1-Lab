'''
Python program to combine each line from first file with the corresponding line in second
file.
'''

with open("file1.txt", "r") as f1:
    with open("file2.txt", "r") as f2:
        for i, j in zip(f1.readlines(), f2.readlines()):
            print(i+j)