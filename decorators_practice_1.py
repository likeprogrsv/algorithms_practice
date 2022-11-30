import time


def decorator(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        et = time.time()
        dt = et - st
        return f'Время работы: {dt}, результат: {res}'
    return wrapper


def euclid_algo(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def fast_euclid_algo(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


euclid = decorator(euclid_algo)
fast_euclid = decorator(fast_euclid_algo)
print(euclid(3, 1831215))
print(fast_euclid(3, 1831215))
