'''
Python program to write a list content to a file.
'''

l = input("Enter the list: ").split()

with open("test.txt", "a") as f:
    for i in l:
        f.write(i+"\n")