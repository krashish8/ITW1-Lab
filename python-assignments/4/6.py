class String1:
    def __init__(self, str):
        self.str = str
    
    def reverse(self):
        s = ""
        for i in self.str:
            s = i + s
        return s
    
strobj = String1("hello")
print(strobj.reverse())