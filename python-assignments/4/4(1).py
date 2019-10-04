class Class1:
    def __init__(self, var1):
        self.var1 = var1
    
class subClass1 (Class1):
    def func(self):
        super(subClass1, self).func()

obj1 = subClass1(123)
print(obj1.var1)