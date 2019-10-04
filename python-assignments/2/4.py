'''
Python program to sort a tuple by its float element.
'''

def func(t):
    return sorted(t, key = lambda x: float(x[1]), reverse = True)

t = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print(func(t))