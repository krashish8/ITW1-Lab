'''
Python program to calculate the harmonic sum of n-1.
'''

n = int(input("Enter the value of n: "))
s = 0
for i in range(1,n):
    s += 1/i
print(s)