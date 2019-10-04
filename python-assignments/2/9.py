'''
Python program to create set difference, union, and intersection of sets
'''

s1 = set(map(int, input("Enter first set: ").split()))
s2 = set(map(int, input("Enter second set: ").split()))
print("Difference: {}, Union: {}, Intersection: {}".format(s1-s2, s1|s2, s1&s2))