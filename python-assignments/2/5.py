'''
Python program to remove an empty tuple(s) from a list of tuples
'''

def func(l):
    ans = []
    for i in l:
        if len(i)!=0:
            ans.append(i)
    return ans

l = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
print(func(l))