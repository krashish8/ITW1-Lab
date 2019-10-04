'''input
2
hello world
line 2
'''

l = [input().upper() for  i in range(int(input("Enter number of lines: \n")))]
for i in l:
    print(i) 