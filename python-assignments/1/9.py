'''
Python function to merge two sorted arrays.
'''

def merge(a,b):
    ans=[]
    i, j = 0, 0
    while i < len(a) and j < len(b):
            if a[i] < b[j]:
                ans.append(a[i])
                i = i + 1
            else:
                ans.append(b[j])
                j = j + 1
    if i == len(a):
        while j < len(b):
            ans.append(b[j])
            j = j + 1
    if j == len(b):
        while i < len(a):
            ans.append(a[i])
            i = i + 1
    return ans

a1 = list(map(int, input("Enter first array: ").split()))
a2 = list(map(int, input("Enter second array: ").split()))
print("Merged array:",merge(a1,a2))