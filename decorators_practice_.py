

def decorator(func):
    def wrapper(*args, **kwargs):
        print('****************')
        func(*args, **kwargs)
        print('****************')
    return wrapper


@decorator
def some_func(title, name):
    print(f'{title}, {name}!')


some_func('Приветсвую в Python', 'Михаил')

