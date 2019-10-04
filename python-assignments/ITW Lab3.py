'''
try:
    print("x")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
finally:
    print("Finished")


def divide(x, y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("Div by 0 error")
    else:
        print("result")
    finally:
        print("Executed")

divide(2,1)
divide(2,0)
divide("2","1")


try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise


class Car:
    total = 0
    def __init__(self, make, model, year):
        Car.total += 1
        self.make = make
        self.model = model
        self.year = year
        print("Instance object of the class is created")
    def display(self):
        print(self.total)
        print(Car.total)
        print("Make:", self.make)
        print("Model:", self.model)
        print("Year:", self.year)
        print()
    def __del__(self):
        Car.total -= 1
        print("Destructed")

obj1 = Car("A", "B", 2019)
print(obj1.make)
obj1.display()

obj2 = Car("C", "D", 2000)
obj2.display()

del obj2

obj3 = Car("H","B","C")
obj3.display()
print("TOTAL:", Car.total)


class Car:
    superString = "Class variable is super class"
    def __init__(self):
        print("Initialied")
    def superMethod(self):
        print("Method of super class is called")

class LuxeriousCar(Car):
    subString = "Class variable of LuxeriousCar class"
    def __init__(self):
        print("Initialization method of LuxeriousCar class is called")
    def subMethod(self):
        print("Method of LuxeriousCar class is called")

class SubLuxeriousCar(LuxeriousCar):
    def __init__(self):
        print("Instance object of SubLuxeriousCar is created")
        
subSubCar = SubLuxeriousCar()
subSubCar.superMethod()
subSubCar.subMethod()


print(0/0)


try:
    print(x)
except NameError:
    print("An exception occured")
except:
    print("Error")
# except must be last

try:
    print(x)
    print(0/0)
except ZeroDivisionError:
    print("Variable x is not defined")
except ZeroDivisionError:
    print("Division by 0 error")
else:
    print("Something is wrong")
'''