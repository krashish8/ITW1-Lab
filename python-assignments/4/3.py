class Class1:
    pass

class Class2 (Class1):
    pass

if issubclass(Class1, Class2):
    print("Class1 is subclass of Class2")
elif issubclass (Class2, Class1):
    print("Class2 is subclass of Class1")