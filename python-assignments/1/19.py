'''
Python program to insert a given string at the beginning of all items in a list.
'''

l = input("Enter the list: ").split()
s = input("Enter the string: ")
for i in range(len(l)):
    l[i] = s + l[i]
print(" ".join(l))