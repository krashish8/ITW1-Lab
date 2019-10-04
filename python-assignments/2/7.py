'''
Python program to count the elements in a list until an element is a tuple
'''

def count(l):
    c = 0
    for i in l:
        if type(i)==type(tuple()):
            break
        c += 1
    return c

l = [10,20,30,(10,20),40]
print(count(l))