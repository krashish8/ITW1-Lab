'''
Python program to remove a specified item using the index from an array.
'''

l = input("Enter the array: ").split()
e = int(input("Enter the index to remove: "))
if e <= len(l):
    l.pop(e)
    print("New array: "+" ".join(l))
else:
    print("Array index out of range")