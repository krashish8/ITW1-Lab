import numpy as np
import matplotlib.pyplot as plt
import random

x = [1,4,9,16]
y = [25,36,49,64]
plt.plot(x,y, marker='o', linestyle = '--',color='b',label='line')
plt.legend(loc = 'lower right')

a = [random.randint(1,50) for i in range(50)]
b = [random.randint(1,50) for i in range(50)]
plt.scatter(a,b)


x = np.random.normal(size = 1000)
plt.hist(x, bins = 50)

x = [0,1,2,3]
y = [5.5,10.2,1.0,2.0]
plt.bar(x,y, color='r')