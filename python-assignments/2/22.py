'''
Generate three random password string of length 10 with special characters, letters, and digits by
using python modules (random and string).
'''

import random
import string

s = string.ascii_letters + string.digits + string.punctuation
for i in range(10):
    print(random.choice(s), end="")