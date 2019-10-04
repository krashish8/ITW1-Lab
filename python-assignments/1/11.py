'''
Python program which accepts a sequence of comma separated 4 digit binary numbers as
its input and print the numbers that are divisible by 5 in a comma separated sequence.
'''

s = input("Enter the sequence: ")
l = s.split(",")
ans = []
for i in l:
    dec = 0
    for j in range(len(i)):
        dec += pow(2,len(i)-j-1)*int(i[j])
    if dec%5==0:
        ans.append(i)
        
print("Divisible by 5: "+",".join(ans))