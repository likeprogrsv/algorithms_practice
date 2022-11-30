import random

arr = [random.randint(0, 61) for i in range(33)]


def func_helper(function):
    def inner(*args, **kwargs):
        result = function(*args, **kwargs)
        return print([i for i in result if i % 3 == 0])
    return inner


@func_helper
def func(array: list):
    return [i for i in array if i % 4 == 0]


print(arr)
func(arr)

