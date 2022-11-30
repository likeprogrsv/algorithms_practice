
def select(func):
    def outter_func(*args):
        print('*************************')
        func(*args)
        print('*************************')
    return outter_func


@select
def do_it(message):
    print(message)


def invert(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        result = list(map(lambda x: -x, result))
        return print(result)
    return wrapper


@invert
def func(length: int):
    is_negative = length < 0
    return [i if not is_negative else -i for i in range(abs(length)) if i % 3 == 0]

# do_it('fffadad')

# def test():
#     assert func(6) == [0, 3]
#     assert func(-7) == [0, -3, -6]
#     print(func(-10))


# print(func(-7))
# func(-10)
# test()
