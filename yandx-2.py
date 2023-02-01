def sort_ascii_array(arr):
    max_char = max([ord(char) for char in arr])
    freq = [0] * (max_char + 1)
    for char in arr:
        freq[ord(char)] += 1
    sorted_arr = []
    for i in range(len(freq)):
        if freq[i] != 0:
            for j in range(freq[i]):
                sorted_arr.append(chr(i))
    return sorted_arr

print(sort_ascii_array(['a', 'd', 'k', 'j', '&']))