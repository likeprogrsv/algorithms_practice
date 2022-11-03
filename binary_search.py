import math
array = [0,1,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


def binarySearch(arr, item):
    start = 0
    end = len(arr) - 1
    middle = 0
    position = -1
    while start <= end:
        middle = math.floor((start + end)/2)
        if arr[middle] == item:
            position = middle
            return position
        if item < arr[middle]:
            end = middle - 1
        else:
            start = middle + 1
    print(f'Element {item} not found')
print(binarySearch(array, 14))

