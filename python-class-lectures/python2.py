#Defining Functions
#The keyword def introduces a function definition
# It must be followed by the function name and the parenthesized list of formal parameters. 
#The statements that form the body of the function start at the next line, and must be indented.
#Structure of a function
def Function_name(b):    # b is formal parameter
  function_body

Function_name(a)         # a is the actual parameter


#Creating a function
def my_function():
  print("My first function") 

#Calling a function
def my_function():
  print("My first function")

my_function()

Output: My first function 

#Default parameter value
def my_function(name = "Randheer"):
  print("I am " + name)

my_function("Rahul")
my_function("Ashish")
my_function()
my_function("Arun") 

Output: I am Rahul
        I am Ashish
        I am Randheer
        I am Arun

# write Fibonacci series up to n
>>> def fib(n):    
...     """Print a Fibonacci series up to n."""  #function’s documentation string, or docstring
...     a, b = 0, 1
...     while a < n:
...         print(a, end=' ')
...         a, b = b, a+b

>>> # Now call the function we just defined:
... fib(2000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597

>>> f = fib
>>> f(100)
0 1 1 2 3 5 8 13 21 34 55 89

#a function that returns a list of the numbers of Fibonacci series, instead of printing it
>>> def fib2(n):  # return Fibonacci series up to n
...     """Return a list containing the Fibonacci series up to n."""
...     result = []
...     a, b = 0, 1
...     while a < n:
...         result.append(a)    # see below
...         a, b = b, a+b
...     return result
...
>>> f100 = fib2(100)    # call it
>>> f100                # write the result
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#The return statement returns with a value from a function. 

#More on Defining Functions:
#It is also possible to define functions with a variable number of arguments. There are three forms, which can be combined.

#Default Argument Values
#The most useful form is to specify a default value for one or more arguments. This creates a function that can be called with fewer arguments than it is defined to allow. For example:

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

#This function can be called in several ways:

    giving only the mandatory argument: ask_ok('Do you really want to quit?')
    giving one of the optional arguments: ask_ok('OK to overwrite the file?', 2)
    or even giving all arguments: ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

#The default values are evaluated at the point of function definition in the defining scope, so that

i = 5

def f(arg=i):
    print(arg)

i = 6
f()

Output: 5

#Example:
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

#This will print

[1]
[1, 2]
[1, 2, 3]


#Keyword Arguments:
#Functions can also be called using keyword arguments of the form kwarg=value. For instance, the following function:

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

#accepts one required argument (voltage) and three optional arguments (state, action, and type). This function can be called in any of the following ways:

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

#but all the following calls would be invalid:

parrot()                     # required argument missing
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument


#Arbitrary Argument Lists

#Finally, the least frequently used option is to specify that a function can be called with an arbitrary number of arguments. These arguments will be wrapped up in a tuple (see Tuples and Sequences). Before the variable number of arguments, zero or more normal arguments may occur.

>>> def concat(*args, sep="/"):
...     return sep.join(args)
...
>>> concat("earth", "mars", "venus")
'earth/mars/venus'
>>> concat("earth", "mars", "venus", sep=".")
'earth.mars.venus'

#Unpacking Argument Lists:

#The reverse situation occurs when the arguments are already in a list or tuple but need to be unpacked for a function call requiring separate positional arguments. For instance, the built-in range() function expects separate start and stop arguments. If they are not available separately, write the function call with the *-operator to unpack the arguments out of a list or tuple:

>>> list(range(3, 6))            # normal call with separate arguments
[3, 4, 5]
>>> args = [3, 6]
>>> list(range(*args))            # call with arguments unpacked from a list
[3, 4, 5]

# Example of unpacking. 
#A function that takes 3 arguments
def fun(a,b,c):
    print('{} {} {}'.format(a, b, c))
    # list of arguments
a = ['Ram', '&', 'Shyam']
# passing the list 
print(fun(a))

Output: fun() missing 2 required positional arguments: 'b' and 'c'

def fun(a,b,c):
    print('{} {} {}'.format(a, b, c))
    # list of arguments
a = ['Ram', '&', 'Shyam']
# passing the list 
print(fun(*a))

Output: Ram & Shyam

#Example of packing
# a function that uses packing to print unknown number of arguments
def friends(*names):
    for name in names:
        print(name)
            
friends('Ram')
friends('Shyam', 'Mohan')

Output: Ram
        Shyam
        Mohan

#In the same fashion, dictionaries can deliver keyword arguments with the **-operator:

>>> def parrot(voltage, state='a stiff', action='voom'):
...     print("-- This parrot wouldn't", action, end=' ')
...     print("if you put", voltage, "volts through it.", end=' ')
...     print("E's", state, "!")
...
>>> d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
>>> parrot(**d)
Output: This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !

#Lambda Expressions:
# lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.

>>> def make_incrementor(n):
...     return lambda x: x + n
...
>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43

#Data Structures:
#Mutable Objects: It can be modified after the creation.
#Examples:
#List
mutable_object = ['a', 'b', 'c']
mutable_object[1] = 'x'
print(mutable_object)

Output: ['a', 'x', 'c']

#Dictonary
mutable_object = {1: 'one', 2: 'two', 3: 'three'}
mutable_object[1] = 'four'
print(mutable_object)

Output: {1: 'four', 2: 'two', 3: 'three'}

#Set
x = set([1, 2, 3])
y = x
y |= set([4, 5, 6])
print('Values of x:', x)
print('Values of y:', y)

Output: Values of x: {1, 2, 3, 4, 5, 6}
        Values of y: {1, 2, 3, 4, 5, 6}

#Immutable Objects:It can not modified after the creation.
#Examples:
#Tuple
immutable_object = ('a', 'b', 'c')
immutable_object[1] = 'x'
print(immutable_object)

Output: immutable_object[1] = 'x'
        TypeError: 'tuple' object does not support item assignment

#String:
immutable_object = 'one'
immutable_object[1] = 'O'
print(immutable_object)

Output: immutable_object[1] = 'O'
        TypeError: 'str' object does not support item assignment

#More on Lists:
#The list data type has some more methods. Here are some of the methods of list objects:

#To creat a list

test = [5, 3, 1, 4, 2]
        0  1  2  3  4   #positive index numbers
       -5 -4 -3 -2 -1   #negative index numbers


#slicing in list
my_list = ['p','r','o','b','e']

print(my_list[0]) # Output: p

print(my_list[2]) # Output: o

print(my_list[4]) # Output: e

print(my_list[4.0]) # Error! Only integer can be used for indexing

# Nested List
n_list = ["Happy", [2,0,1,5]]

# Nested indexing

print(n_list[0][1])  # Output: a  

print(n_list[1][3])  # Output: 5

#Negative indexing
my_list = ['p','r','o','b','e']

print(my_list[-1])  # Output: e

print(my_list[-5]) # Output: p

#More in slicing

my_list = ['p','r','o','g','r','a','m','i','t']

print(my_list[2:5])  # elements 3rd to 5th

print(my_list[:-5])  # elements beginning to 4th

print(my_list[5:])   # elements 6th to end

print(my_list[:])    # elements beginning to end 

#More operations in list
list.append(x)

    #Add an item to the end of the list. Equivalent to a[len(a):] = [x].

list.insert(i, x)

#Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

list.remove(x)

#Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

list.pop([i])

    #Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

list.clear()

    #Remove all items from the list. Equivalent to del a[:].


list.count(x)

    #Return the number of times x appears in the list.

list.sort(key=None, reverse=False)

    #Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

list.reverse()

    #Reverse the elements of the list in place.

list.copy()

    #Return a shallow copy of the list. Equivalent to a[:].

#Some examples that uses most of the list methods:

>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>> fruits.count('tangerine')
0
>>> fruits.index('banana')
3
>>> fruits.index('banana', 4)  # Find next banana starting a position 4
6
>>> fruits.reverse()
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grape')
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear'

#You might have noticed that methods like insert, remove or sort that only modify the list have no return value printed – they return the default None. This is a design principle for all mutable data structures in Python.

#Using Lists as Stacks

#The list methods make it very easy to use a list as a stack, where the last element added is the first element retrieved (“last-in, first-out”). For example:

>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]

#Using Lists as Queues:

#It is also possible to use a list as a queue, where the first element added is the first element retrieved (“first-in, first-out”); however, lists are not efficient for this purpose. While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one).

#To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends. For example:

>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])

#List Comprehensions:

#List comprehensions provide a concise way to create lists.
#For example, assume we want to create a list of squares, like:

>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#Note that, this creates (or overwrites) a variable named x that still exists after the loop completes. We can calculate the list of squares without any side effects using:

squares = list(map(lambda x: x**2, range(10)))

or, equivalently:

squares = [x**2 for x in range(10)]

#which is more concise and readable.

#A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it. For example, this listcomp combines the elements of two lists if they are not equal:

>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

#and it’s equivalent to:

>>> combs = []
>>> for x in [1,2,3]:
...     for y in [3,1,4]:
...         if x != y:
...             combs.append((x, y))
...
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

#Note how the order of the for and if statements is the same in both these snippets.

#If the expression is a tuple (e.g. the (x, y) in the previous example), it must be parenthesized.

>>> vec = [-4, -2, 0, 2, 4]
>>> # create a new list with the values doubled
>>> [x*2 for x in vec]
[-8, -4, 0, 4, 8]
>>> # filter the list to exclude negative numbers
>>> [x for x in vec if x >= 0]
[0, 2, 4]
>>> # apply a function to all the elements
>>> [abs(x) for x in vec]
[4, 2, 0, 2, 4]
>>> # call a method on each element
>>> freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
>>> [x.strip() for x in freshfruit]
['banana', 'loganberry', 'passion fruit']
>>> # create a list of 2-tuples like (number, square)
>>> [(x, x**2) for x in range(6)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
>>> # the tuple must be parenthesized, otherwise an error is raised
>>> [x, x**2 for x in range(6)]
  File "<stdin>", line 1, in <module>
    [x, x**2 for x in range(6)]
               ^
SyntaxError: invalid syntax

#List comprehensions can contain complex expressions and nested functions:

from math import pi
print([(round(pi, i)) for i in range(1, 6)])
[3.1, 3.14, 3.142, 3.1416, 3.14159]


#The del statement:
#There is a way to remove an item from a list given its index instead of its value: the del statement. This differs from the pop() method which returns a value. The del statement can also be used to remove slices from a list or clear the entire list (which we did earlier by assignment of an empty list to the slice). For example:

>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
#del can also be used to delete entire variables:

>>> del a

#Tuples and Sequences:
#We saw that lists and strings have many common properties, such as indexing and slicing operations. They are two examples of sequence data types (see Sequence Types — list, tuple, range). Since Python is an evolving language, other sequence data types may be added. There is also another standard sequence data type: the tuple.

#A tuple consists of a number of values separated by commas, for instance:

>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> # Tuples may be nested:
... u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> # Tuples are immutable:
... t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> # but they can contain mutable objects:
... v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])

#Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking or indexing. Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.

#A special problem is the construction of tuples containing 0 or 1 items: the syntax has some extra quirks to accommodate these. Empty tuples are constructed by an empty pair of parentheses; a tuple with one item is constructed by following a value with a comma (it is not sufficient to enclose a single value in parentheses). Ugly, but effective. For example:

>>> empty = ()
>>> singleton = 'hello',    # <-- note trailing comma
>>> len(empty)
0
>>> len(singleton)
1
>>> singleton
('hello',)

#The statement t = 12345, 54321, 'hello!' is an example of tuple packing: the values 12345, 54321 and 'hello!' are packed together in a tuple. 

#Sets:
#A set is an unordered collection with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

#Curly braces or the set() function can be used to create sets. Note: to create an empty set you have to use set(), not {};

#Here is a brief demonstration:

>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket                 # fast membership testing
True
>>> 'crabgrass' in basket
False

>>> # Demonstrate set operations on unique letters from two words
...
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # letters in a but not in b (difference)
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both (union)
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b (intersection)
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both (symmetric difference)
{'r', 'd', 'b', 'm', 'z', 'l'}

#Similarly to list comprehensions, set comprehensions are also supported:

>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}

#Dictionaries:
#It is best to think of a dictionary as a set of key: value pairs, with the requirement that the keys are unique (within one dictionary). 

#The main operations on a dictionary are storing a value with some key and extracting the value given the key. 

#Performing list(d) on a dictionary returns a list of all the keys used in the dictionary, in insertion order (if you want it sorted, just use sorted(d) instead). To check whether a single key is in the dictionary, use the in keyword.

#Here is a small example using a dictionary:

>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
>>> list(tel)
['jack', 'guido', 'irv']
>>> sorted(tel)
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False

#The dict() constructor builds dictionaries directly from sequences of key-value pairs:

>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}

#In addition, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:

>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}

#When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:

>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}

#Looping Techniques:
#When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the items() method.

>>> knights = {'gagan': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)
...
gagan the pure
robin the brave

#When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function.

>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe

#To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the reversed() function.
>>> for i in reversed(range(1, 10, 2)):
...     print(i)
...
9
7
5
3
1

#To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered.

>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
...     print(f)
...
apple
banana
orange
pear


#More on Conditions:
#It is possible to assign the result of a comparison or other Boolean expression to a variable. For example,

>>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
>>> non_null = string1 or string2 or string3
>>> non_null
'Trondheim'

#Module: A collection of related functions, python definition and statements, that are placed in their own file.

Example:
# A simple module, calc.py 
  
def add(x, y): 
    return (x+y) 
  
def subtract(x, y): 
    return (x-y) 

# importing  module calc.py 
import calc 
  
print add(10, 2) 

# Fibonacci numbers module as fibo.py
Example:
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
#Now enter the Python interpreter and import this module with the following command:
>>>import fibo

#This does not enter the names of the functions defined in fibo directly in the current symbol table; it only enters the module name fibo there. Using the module name you can access the functions:
>>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#More in Module:
>>> from fibo import *
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

#If the module name is followed by as, then the name following as is bound directly to the imported module.
>>> import fibo as fib
>>> fib.fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

#It can also be used when utilising from with similar effects:
>>> from fibo import fib as fibonacci
>>> fibonacci(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
 
Standard Modules:

# importing sqrt() and factorial from the 
# module math 
from math import sqrt, factorial 

# if we simply do "import math", then 
# math.sqrt(16) and math.factorial() 
# are required. 
print sqrt(16) 
print factorial(6) 

#The dir() Function:

#The built-in function dir() is used to find out which names a module defines. It returns a sorted list of strings:

>>> import math
>>> dir(math)
['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']

#Python built-in-module:
# importing built-in module math 
import math 

# using square root(sqrt) function contained 
# in math module 
print (math.sqrt(25)) 

# using pi function contained in math module 
print (math.pi) 

# 1 * 2 * 3 * 4 = 24 
print (math.factorial(4)) 

#find the floating sum of a list
import math
value = [0.325, 1, 2]
result= math.fsum(value)
print(result)

# importing built in module random 
import random 

# printing random integer between 0 and 5 
print (random.randint(0, 5)) 

# print random floating point number between 0 and 1 
print (random.random()) 

# roll a die

import random
min =1; 
max =6;
result= random.randint(min, max)
print(result)

#print today's date and current time with date
import datetime
print(datetime.date.today())
print(datetime.datetime.now())
















