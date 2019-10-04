'''
Python program to sort a list of elements using the bubble sort algorithm
'''

a = list(map(int, input("Enter the list: ").split()))
n = len(a)
for i in range(0,n-1):
    for j in range(0,n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)