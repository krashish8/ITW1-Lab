'''
Python program to compute the similarity between two lists
'''

l1 = input("Enter first list: ").split()
l2 = input("Enter second list: ").split()
print("Color1 - Color2: " + " ".join([i for i in l1 if i not in l2]))
print("Color2 - Color1: " + " ".join([i for i in l2 if i not in l1]))