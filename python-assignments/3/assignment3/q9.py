color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

with open('output.txt', 'w') as f:
    for i in color:
        f.write(i + '\n')

with open('output.txt') as f:
    print(f.read())
