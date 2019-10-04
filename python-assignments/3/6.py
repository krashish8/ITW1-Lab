'''
Python program to count the number of lines in a text file
'''

with open("test.txt", "r") as f:
    print(len(f.readlines()))