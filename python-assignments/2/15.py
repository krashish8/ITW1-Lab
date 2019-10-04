'''
Python program to sort a list of elements using the selection sort algorithm
'''

a = list(map(int, input("Enter the list: ").split()))
n = len(a)
for i in range(0,n-1):
    m = a[i]
    pos = i
    for j in range(i+1,n):
        if m > a[j]:
            m = a[j]
            pos = j
    a[i], a[pos] = a[pos], a[i]
print(a)