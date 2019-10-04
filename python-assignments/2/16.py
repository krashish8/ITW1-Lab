'''
Python program to sort a list of elements using the merge sort algorithm
'''

def merge(a, start, mid, end):
    p, q = start, mid + 1
    arr = []
    for i in range(start, end+1):
        if p > mid:
            arr.append(a[q])
            q += 1
        elif q > end:
            arr.append(a[p])
            p += 1
        elif a[p] < a[q]:
            arr.append(a[p])
            p += 1
        else:
            arr.append(a[q])
            q += 1
    for i in range(start, end + 1):
        a[i] = arr[i-start]


def merge_sort(a, start, end):
    if (start < end):
        mid = (start + end)//2
        merge_sort(a, start, mid)
        merge_sort(a, mid+1, end)
        merge(a, start, mid, end)

a = list(map(int, input("Enter the list: ").split()))
merge_sort(a, 0, len(a)-1)
print(a)