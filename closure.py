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