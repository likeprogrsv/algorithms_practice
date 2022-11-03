import random

array = [random.randint(-4, 5) for i in range(9)]


def selectSort(arr):
    for i in range(len(arr)):
        index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[index]:
                index = j
        arr[i], arr[index] = arr[index], arr[i]


selectSort(array)
print(array)