'''
Python program to split a list every Nth element
'''

l = input("Enter the list: ").split()
N = int(input("Enter N: "))
ans = []
for i in range(N):
    ans.append(l[i::N])
print(ans)