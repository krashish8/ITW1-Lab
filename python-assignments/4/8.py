class PairSum:
    def __init__(self, arr):
        self.arr = arr
    
    def findSum(self, target):
        a = self.arr
        l = []
        for i in range(0, len(a)):
            for j in range(i+1, len(a)):
                if (a[i] + a[j] == target):
                    l.append([i+1, j+1])
        return l

arr = PairSum([10,20,10,40,50,60,70])
print(arr.findSum(50))