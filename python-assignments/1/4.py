'''
Python function to insert a string in the middle of a string
'''

def insert_string_middle(s1, s2):
    pos = len(s1)//2
    s1 = s1[:pos] + s2 + s1[pos:]
    return s1

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print("Final string: "+insert_string_middle(s1,s2))