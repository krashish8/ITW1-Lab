import numpy as np
n = int(input("Enter no of rows:"))
l = [0 for i in range(0, n*n)]
for i in range(0, n):
    l[i] = 1
for i in range(n*n-n, n*n):
    l[i] = 1
for i in range(0,n*n,n):
    l[i] = 1
for i in range(n-1,n*n,n):
    l[i] = 1
arr = np.array(l).reshape(n,n)
print(arr)