with open('test.txt') as f:
    n = input("Enter Number of line")
    for i in range(int(n)):
        try:
            print(f.readline(), end="")
        except:
            break
