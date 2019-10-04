﻿import numpy as np
arr = np.array([10,45,1,65,78,10,56,4,5]).reshape(3,3)
print("Array:")
print(arr)
print("Sorted along first axis:")
print(np.sort(arr, axis = 0))
print("Sorted along last axis: ")
print(np.sort(arr, axis = -1))
print("Flattened array:")
print(np.sort(arr.flat))