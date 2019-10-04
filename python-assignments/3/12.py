'''
program that accepts sequence of lines as input and prints the lines after making all
characters in the sentence capitalized
'''

l = int(input("Enter the number of lines: "))
print("Enter the sequence of lines:")

ans = []

for i in range(l):
    s = input()
    ans.append(s.upper())
    
for i in ans:
    print(i)