import random
#arr = [random.randint(-3, 5) for i in range(6)]
arr = ['see', 'a', 'fish', 'joke', 'pass', 'egg', 'jack']

def quick_sort(array, lo_indx=None, hi_indx=None):
    if lo_indx is None:
        lo_indx = 0
    if hi_indx is None:
        hi_indx = len(array) - 1
    if lo_indx >= hi_indx:
        return None

    p = partition(array, lo_indx, hi_indx)
    quick_sort(array, lo_indx, p - 1)
    quick_sort(array, p + 1, hi_indx)


def partition(array, lo_indx, hi_indx):
    support_element = array[lo_indx]
    i = lo_indx + 1
    j = hi_indx
    while True:
        while array[i] < support_element and i < hi_indx:
            i += 1
        while array[j] > support_element:
            j -= 1
        if i >= j:
            break
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1
    array[lo_indx], array[j] = array[j], array[lo_indx]
    return j


def binary_search(array, item):
    start = 0
    end = len(array) - 1
    while start <= end:
        middle = (start + end) // 2
        if array[middle] == item:
            return f'Index position of required item "{item}"  is {middle}'
        if array[middle] > item:
            end = middle - 1
        if array[middle] < item:
            start = middle + 1
    return f'Element {item} not found'


print(arr)
quick_sort(arr)
print(arr)
print(binary_search(arr, 'j'))
