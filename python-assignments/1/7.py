'''
Python function that prints out the first ‘n’ rows of Pascal's triangle. ‘n’ is user input
'''

def Pascal_Triangle(n):
    for i in range(n):
        print(" "*(n-i),end="")
        for j in range(i+1):
            print(str(ncr(i,j))+" ", end = "")
        print()
    
def fact(n):
    p = 1
    for i in range(1,n+1):
        p = p*i
    return p

def ncr(n,r):
    return int(fact(n)/fact(r)/fact(n-r))

n = int(input("Enter the number of rows: "))
Pascal_Triangle(n)