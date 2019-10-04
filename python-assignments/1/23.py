'''
Python program to iterate over two lists simultaneously.
'''

a = input("Enter first list: ").split()
b = input("Enter second list: ").split()
for i in range(min(len(a),len(b))):
    print(a[i],b[i])