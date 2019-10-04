import numpy as np
source = np.array([0,40])
arr = np.array([10,10,20,30,30])
arr.put([0,4],source)
print(arr)