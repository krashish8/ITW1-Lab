class Num:
    def __init__(self, n):
        self.n = n
    def value(c):
        if c >= '0' and c <= '9':
            return ord(c)-48
        else:
            return (ord(c)-65+10)
    
    def hexToDec(self):
        dec = 0
        c = 0
        s = self.n
        for i in range(len(s)-1, -1, -1):
            dec += Num.value(s[i])*(16**c)
            c += 1
        return dec

n = input("Enter a number in hexadecimal: ")
obj = Num(n)
print("Decimal form:",obj.hexToDec())