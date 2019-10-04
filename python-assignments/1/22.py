'''
Python program to convert a list of multiple integers into a single integer
'''

l = list(map(int,input("Enter the list: ").split()))
ans = 0
for i in l:
    ans = ans*(10**len(str(i)))+i
print(ans)