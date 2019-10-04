'''
Python program to replace dictionary values with their sum.
'''

def rep(l):
    for d in l:
        n1 = d.pop('V')
        n2 = d.pop('VI')
        d['V + VI'] = (n1+n2)/2
    return l

l = [{'id' : 1, 'subject' : 'math', 'V' : 70, 'VI': 82},
{'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
{'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}]
print(rep(l))