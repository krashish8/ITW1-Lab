'''
Python program to count repeated characters in a string.
'''
s = input("Enter the string: ")
freq = {}
for i in s:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
for key, value in freq.items():
    if value > 1:
        print(key, value)