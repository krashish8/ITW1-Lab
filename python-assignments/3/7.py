'''
Python program to count the frequency of words in a file.
'''

import string
def removePunc(w):
    s = string.punctuation
    ans = ""
    for c in w:
        if c not in s:
            ans = ans + c
    return ans

with open("test.txt", "r") as f:
    l = f.read().split()
    freq = dict()
    for i in l:
        i = removePunc(i)
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    print(freq)
    
