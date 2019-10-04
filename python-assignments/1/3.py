"""
Python program to find the first appearance of the substring 'not' and 'poor' from a given
string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the
resulting string.
"""

s = input("Enter the string: ")
i = s.find('not')
j = s.find('poor')
if i < j:
    print ("Result: "+s[:i] + "good" + s[j+4:])
else:
    print ("Result: "+s)