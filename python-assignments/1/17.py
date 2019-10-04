'''
Python program to remove duplicates from a list of lists.
'''

def remove_duplicates(l):
    ans = []
    for i in range(len(l)):
        found = 0
        for j in range(i):
            if(l[i]==l[j]):
                found = 1
        if found==0:
            ans.append(l[i])
    return ans

l = [[10,20],[40],[30,56,25],[10,20],[33],[40]]
print(remove_duplicates(l))