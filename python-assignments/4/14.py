import numpy as np
a1 = [1,2,3,4]
a2 = ['Red', 'Green', 'White', 'Orange']
a3 = [12.20,15,20,40]
arr = np.stack((a1,a2,a3), axis = 1)
print(arr)