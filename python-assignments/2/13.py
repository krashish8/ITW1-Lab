'''
Python program for binary search
'''

a = list(map(int, input("Enter the sorted list of numbers: ").split()))
s = int(input("Enter the number to search: "))
l, r = 0, len(a)
while l <= r:
    mid = (l+r)//2
    if a[mid] == s:
        print("%d was found at index %d" % (s, mid))
        break
    elif s > a[mid]:
        l = mid + 1
    else:
        r = mid - 1
if l > r:
    print("Element not found")