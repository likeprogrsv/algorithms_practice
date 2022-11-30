"""
def outer():
    i = 6
    def inner():
        nonlocal i
        i += 8
        print(i)
    return inner

func = outer()
func()
func1 = outer()
func()
func1()
"""


def outer(message_1):
    def inner(message_2):
        print(f'{message_1} {message_2}')
    return inner


func = outer('Я во внешней функции')
func('и во внутренней функции')
func1 = outer('Ещё один объект')
func1('c внтуренней функцией')
