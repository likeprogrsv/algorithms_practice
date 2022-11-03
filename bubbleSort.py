arr = [0, 3, 2, 5, 6, 8, 1, 9, 4, 2, 1, 2, 9, 6, 4, 1, 7, -1, -5, 23, 6, 2, 35, 6, 3, 32]



def bubbleSort(array):
    count = 0
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j + 1] < array[j]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j+1] = temp
            count += 1

    print(count)
    return array

print(bubbleSort(arr))
print(len(arr))