'''
Python program to convert a list of tuples into a dictionary
'''

def convert(l):
    d = {}
    for i in l:
        d[i[1]] = i[0]
    return d

l = ((2, "w"),(3, "r"))
print(convert(l))