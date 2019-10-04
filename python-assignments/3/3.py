'''
Python program to append text to a file and display the text
'''

with open("myfile.txt", "a") as f:
    s = input("Enter the string: ")
    f.write(s)

with open("myfile.txt", "r") as f:
    print(f.read())