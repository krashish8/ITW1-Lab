s = input("Enter string to append")

with open('myfile.txt', 'a') as f:
    f.write('\n')
    f.write(s)

with open('myfile.txt') as f:
    print(f.read())