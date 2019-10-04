'''
Python program using functions that asks the user for a long string containing multiple
words. Print back to the user the same string, except with the words in backwards order
'''

def reverseWords(s):
    l = list(s.split())
    return " ".join(l[::-1])
    
s = input("Enter the string: ")
print(reverseWords(s))