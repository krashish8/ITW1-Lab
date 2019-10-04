'''
Python program to find the available built-in modules
'''

import sys
def memSize(s):
    return sys.getsizeof(s)

s = input("Enter the string: ")
print("Memory size of '%s' = %d bytes" % (s, memSize(s)))
