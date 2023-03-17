import copy
test_1 = [1, 2, 3, [1, 2, 3]]
test_copy = copy.copy(test_1)
print(test_1, test_copy)


test_copy.append(4)
print(test_1, test_copy)

test_copy[0] = 56
print(test_1, test_copy)


test_1 = [1, 2, 3, [1, 2, 3]]
test_deepcopy = copy.deepcopy(test_1)
test_deepcopy[3].append(4)
print(test_1, test_deepcopy)