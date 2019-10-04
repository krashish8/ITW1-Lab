'''
Python function that accepts a hyphen-separated sequence of words as input and prints the
words in a hyphen-separated sequence after sorting them alphabetically.
'''

def func(s):
    l = s.split("-")
    l.sort()
    print("-".join(l))
    
s = input("Enter the sequence of words: ")
func(s)