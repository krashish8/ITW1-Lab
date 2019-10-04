'''
Python program to insert a new item before the second element in an existing array.
'''

l = input("Enter the elements of list: ").split()
i = input("Enter the new item: ")
l.insert(1,i)
print("New list: "+" ".join(l))