'''
Python program to match key values in two dictionaries
'''

def func (d1, d2):
    print("Key-value pair present in both dictionary:")
    for key, value in d1.items():
        if key in d2 and d2[key]==value:
            print(str(key) + ": " + str(value))

d1 = {'key1': 1, 'key2': 3, 'key3': 2}
d2 = {'key1': 1, 'key2': 2}
func(d1, d2)