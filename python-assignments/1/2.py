"""
Python program to get a string from a given string where all occurrences of its first char have
been changed to '$', except the first char itself
"""

s = input("Enter the string: ")
t = ""
for i in range(len(s)):
    if i == 0:
        t = t + s[i]
    elif s[i] == s[0]:
        t = t + "$"
    else:
        t = t + s[i]
print("Expected string: "+t)