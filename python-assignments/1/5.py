'''
Python program to sort a string lexicographically.
'''
s = input("Enter the string: ")
l = list(s)
l.sort()
print ("".join(l))