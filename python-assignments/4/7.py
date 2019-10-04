class Num:
    def __init__(self, arr):
        self.arr = arr
    
    def sumZero(self):
        a = self.arr
        l = []
        for i in range(0,len(a)):
            for j in range(i+1, len(a)):
                for k in range(j+1, len(a)):
                    if a[i] + a[j] + a[k] == 0:
                        l.append([a[i],a[j],a[k]])
        return l
    
s = Num([-25, -10, -7, -3, 2, 4, 8, 10])
print(s.sumZero())