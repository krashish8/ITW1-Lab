'''
Define a function reverse() that computes the reversal of a string
'''

def reverse(s):
    ans = ""
    for i in s:
        ans  = i + ans
    return ans

s = input("Enter the string: ")
print(reverse(s))