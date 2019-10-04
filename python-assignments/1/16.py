'''
Python program to convert an array to an ordinary list with the same items
'''

from array import *
arr = array('i',[1,2,3,4,5])
l = arr.tolist()
print(l)