'''
Python function that accepts a string and calculate the number of upper case letters and
lower case letters.
'''

def str_count(s):
    u, l = 0, 0
    for i in s:
        if ord(i)>=65 and ord(i)<=90:
            u = u + 1
        if ord(i)>=97 and ord(i)<=122:
            l = l + 1
    return u, l

s = input("Enter the string: ")
print("Upper case letters:", str_count(s)[0])
print("Lower case letters:", str_count(s)[1])