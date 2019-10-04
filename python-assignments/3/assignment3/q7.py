with open('test.txt') as f:
    freq = dict()

    for i in f.read().split():

        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1


for key, val in freq.items():
    print(key, ':', val)
