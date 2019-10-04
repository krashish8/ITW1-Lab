'''
Python program to find the list in a list of lists whose sum of elements is the highest
'''

def max_sum(l):
    ans = l[0]
    s_max = sum(ans)
    for i in l:
        if sum(i) > s_max:
            s_max = sum(i)
            ans = i
    return ans

l = [[1,2,3],[4,5,6],[10,11,12],[7,8,9]]
print(max_sum(l))
