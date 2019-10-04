def convert(n):
    c = 0
    while n >= 1024:
        n /= 1024
        c = c+1
    print(n)

import os
convert(os.path.getsize("a.py"))