'''
Python program of recursion list sum.
'''

def recursion_sum(l):
    ans = 0
    for i in l:
        if type(i)==type(list()):
            ans += recursion_sum(i)
        else:
            ans += i
    return ans

l = [1, 2, [3,4], [5,6]]
print(recursion_sum(l))