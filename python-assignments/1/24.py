'''
Python program to create a list by concatenating a given list which range goes from 1 to n.
'''

l = input("Enter the list: ").split()
n = int(input("Enter the value of n: "))
ans = []
for i in range(1,n+1):
    for j in l:
        ans.append(j+str(i))
print(ans)