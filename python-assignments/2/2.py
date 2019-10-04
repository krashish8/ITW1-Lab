'''
Python program to create a dictionary from two lists without losing duplicate values
'''

def merge(l1, l2):
	d = {}
	for i, j in zip(l1, l2):
		d[i] = j 
	return d 

l1 = input("Enter first list: ").split()
l2 = input("Enter second list: ").split()
print(merge(l1, l2))