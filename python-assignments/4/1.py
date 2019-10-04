class Py1:
    var1 = 10   # Class Variable

obj1 = Py1()
print("Initial var1:", obj1.var1)
obj1.var1 = 20      # Changing class variable
print("Changed var1:", obj1.var1)

# Empty Class
class Empty:
    pass

obj2 = Empty()
