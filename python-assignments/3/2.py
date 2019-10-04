'''
Python program to read first n lines of a file.
'''

with open("test.txt", "r") as f:
    n = int(input("Enter number of lines: "))
    for i in range(n):
        print(f.readline(), end = "")