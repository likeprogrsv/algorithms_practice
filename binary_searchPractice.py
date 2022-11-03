arr = [0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def binary_practice(array, item):
    start = 0
    end = len(array) - 1
    while start <= end:
        middle = (start + end) // 2
        if array[middle] == item:
            return middle
        if item > array[middle]:
            start = middle + 1
        if item < array[middle]:
            end = middle - 1
    return f'Element {item} not found'


print(binary_practice(arr, 51))
