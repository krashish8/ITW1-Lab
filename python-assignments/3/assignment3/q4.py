with open('test.txt') as f:
    n = int(input("Enter number of lines to read from last"))
    try:
        for i in f.readlines()[-n:]:
            print(i, end='')
    except:
        print('ERROR')