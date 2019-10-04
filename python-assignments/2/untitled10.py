'''
Using the module random and time in python generate a random date between given start and end
dates.
'''

from datetime import timedelta
import random

date1 = input("Enter start date: ")
date2 = input("Enter end date: ")
d_format = "%m/%d/%Y"
d0 = datetime.strptime(date1, d_format)
d1 = datetime.strptime(date2, d_format)
print(d0)
diff = (d1 - d0).days
add = random.randint(1,diff)
ans =  d0 + timedelta(days=add)
print("{:%m/%d/%Y}".format(ans))