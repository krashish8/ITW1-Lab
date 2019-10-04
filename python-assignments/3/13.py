'''
python code to split the word from the input file.
'''

import string
def removePunc(w):
    s = string.punctuation
    ans = ""
    for c in w:
        if c not in s:
            ans = ans + c
    return ans

ans = []

with open("test.txt", "r") as f:
    l = f.read().split()
    for i in l:
        i = removePunc(i)
        ans.append(i)

print(ans)