'''
Python program to print alphabet pattern 'R'.
'''

size = int(input("Enter the size: "))
up = (size+1)//2
down = size-up
print("*"*up)
for i in range(up-2):
    print("*"+" "*(up-1)+"*")
print("*"*up)
for i in range(down):
    print("*"+" "*i+"*")