#arr = [0, 3, 2, 5, 6, 8, 1, 9, 4, 2, 1, 2, 9, 6, 4, 1, 7, -1, -5, 23, 6, 2, 35, 6, 3, 32]
arr = [5, 2, -3, 1, -1, 6, 4]


def selectionSort(array):
    count = 0
    for i in range(len(array)):
        indexmin = i
        for j in range(i + 1, len(array)):
            if array[j] < array[indexmin]:
                indexmin = j
            count += 1
        temp = array[i]
        array[i] = array[indexmin]
        array[indexmin] = temp
    print(count)
    return array


#selectionSort(arr)
print(selectionSort(arr))
print(len(arr))
