import math
from random import shuffle
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
'''

print(dir(math))



l = [1,2,3,4,5,6]
shuffle(l)
print(l)

Numpy - ndarray as data structure
pandas - dataframe

print(np.full((2,3),6))
print(np.eye(2,3))


v = np.array([9,10])
w = np.array([1,2])
print(v.dot(w))
print(np.dot(v,w))


# Broadcasting
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
v = np.array([1,0,1])
print(x+v)


dict = {'a':1,'c':6,'e':89,'g':8}
print(pd.Series(dict))


data = [1,2,3,45,6]
idx = [9,8,7,4,5]
print(pd.Series(data,index = idx))


s1 = pd.Series([1,5,6,3,5])
s2 = pd.Series([1.1,3.5,6.5])
s3 = pd.Series(['a','b','c','d'])
data = {'first':s1, 'second':s2, 'third':s3}
print(data)
print(pd.DataFrame(data))


x = np.array([1,12,3])
print(x.dtype)

#making data frame from csv file
pd.read_csv("name.csv", index_col = "Column Name")
#retieving row by loc method
first = data.loc["Name1"]
second = data.loc["Name2"]

# checking for missing values using isnull() or notnull()   --> returns True or False for each value in the Data Set

print(np.nan)

#MATPLOTLIB
'''
x = [5,2,9,4,7]
y = [10,5,8,4,2]
'''
plt.plot(x,y)
plt.show()

plt.bar(x,y)


plt.scatter(x,y)

t = np.arange(1,6,0.3)
plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^') #bs - blue square
# g^   -  green cap
# r--  -  red dash


fin.readline()  --- reads one line and moves 'fin' pointer to another line

self  --> all methods have self parameter, python's reference to the object that invoked the method


class Class1:
    number = 10
    def __init__(self, var1):
        self.var1 = var1
    
class subClass1 (Class1):
    def func(self):
        super(subClass1, self).func()

obj1 = subClass1(123)
print(obj1.number)


print('horse'+'shoe')
print([1,2]+[3])
print([8, 5]*3)
'u' in x   # check for membership
enumerate ----


print(max('bug'))  --> 'u'
print(max(['pigggggg', 'hi', 'there'])) -- > 'there'
print('hippo'.count('p')) --> 2    # same in case of list
print(x.index('p')) # returns index of first p, otherwise "ValueError: substring not found"

# packing: x = [123,5468,498]
# unpacking: a,b,c, = x  (unpack n items of a sequence into n variables)
list - mutable
string - immutable
# constructor - creating a new list: list((1,2,3))
# list creation using comprehensions: x = [m for m in range(8)]
# remove : remove first instance of an item
# x.reverse(): reverse a list
# clear(): delete all items from the list

x.items: returns list of key-value tuple pairs
x.keys

# check type: type(x) --> class, float, int
# id - gives memory location where it is stored
# swapping: x, y = y, x
# bool(x): True or False
False: 0, ''

N O T   W O R K I N G

class A(object):
    x = 10
    def __init__(self):
        print("Parent")
    
class B(A):
    def __init(self):
        print(super().__init__())
        print("HG")
        print(A.x)

obj = B()


'''

