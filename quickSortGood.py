arr = [0, 3, 2, 5, 6, 8, 23, 9, 4, 2, 1, 2, 9, 6, 4, 1, 7, -1, -5, 23, 6, 2, 35, 6, 3, 32, 9, 4, 2, 1, 2, 9, 6, 4, 1, 7,
       -1, -5, 23, 9, 4, 2, 1, 2, 9, 6, 4, 1, 7, -1, -5, 23, ]


def quick_sort(array, lo_index=None, hi_index=None):
    if lo_index is None:
        lo_index = 0
    if hi_index is None:
        hi_index = len(array) - 1
    if lo_index >= hi_index:
        return None
    h = partition(array, lo_index, hi_index)
    quick_sort(array, lo_index, h - 1)
    quick_sort(array, h + 1, hi_index)


def partition(array, lo_index, hi_index):
    support_element = array[lo_index]
    i = lo_index + 1
    j = hi_index
    while True:
        while array[i] < support_element and i < hi_index:
            i += 1
        while array[j] > support_element:
            j -= 1
        if i >= j:
            break
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1
    array[lo_index], array[j] = array[j], array[lo_index]
    return j


quick_sort(arr)
print(arr)
