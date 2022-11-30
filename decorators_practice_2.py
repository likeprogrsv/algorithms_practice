import math
from functools import wraps


def df_decorator(dx=0.01):
    def decorator(func):
        @wraps(func)
        def wrapper(x, *args, **kwargs):
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res
        return wrapper
    return decorator


@df_decorator(dx=0.1)
def sin_df(x):
    """Вычисление производной"""
    return math.sin(x)


df = sin_df(math.pi/4)
print(df)

"""Пример работы декоратора @wraps который сохраняет имя и описание декорируемой функции"""
print(sin_df.__name__)
print(sin_df.__doc__)

"""Можно раскомментить для другого способа декарирования функции"""
# f = df_decorator(dx=0.00001)
# sin_df = f(sin_df)
# df = sin_df(math.pi/4)

""" А можно записать в две строки """
# sin_df = df_decorator(dx=0.0001)(sin_df)
# df = sin_df(math.pi/4)
