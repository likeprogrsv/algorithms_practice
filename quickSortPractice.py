import random

#arr = [random.randint(-32, 24) for i in range(23)]
#arr = [5, -2, -1, 3, 1, 4, 6]
array = [random.randint(-12, 23) for i in range(15)]


def quickSort(arr, lo_indx=None, hi_indx=None):
    if lo_indx is None:
        lo_indx = 0
    if hi_indx is None:
        hi_indx = len(arr) - 1
    if lo_indx >= hi_indx:
        return None

    p = partition(arr, lo_indx, hi_indx)
    quickSort(arr, lo_indx, p - 1)
    quickSort(arr, p + 1, hi_indx)


def partition(arr, lo, hi):
    support_element = arr[lo]
    i = lo + 1
    j = hi
    while True:
        while arr[i] < support_element and i < hi:
            i += 1
        while arr[j] > support_element:
            j -= 1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    arr[lo], arr[j] = arr[j], arr[lo]
    return j


quickSort(array)
print(array)
