
def select(func):
    def outter_func(*args):
        print('*************************')
        func(*args)
        print('*************************')
    return outter_func


@select
def do_it(message):
    print(message)

do_it("I'm here")
