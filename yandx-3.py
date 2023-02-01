def find_maximum(arr):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        c = (mid + 1) % len(arr)
        if arr[mid] > arr[mid - 1] and arr[mid] > arr[(mid + 1) % len(arr)]:
            return arr[mid]
        elif arr[mid] < arr[end]:
            end = mid - 1
        else:
            start = mid + 1
    return None


find_maximum([1,2,3,4,5,6,7,8,])