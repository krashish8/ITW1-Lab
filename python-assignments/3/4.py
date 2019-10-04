'''
Python program to read last n lines of a file.
'''

with open("test.txt", "r") as f:
    n = int(input("Enter number of lines from last to read: "))
    for i in f.readlines()[-n:]:
        print(i, end = "")