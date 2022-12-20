class SingletonFive:
    __instance = []

    def __new__(cls, *args, **kwargs):
        if len(cls.__instance) < 5:
            cls.__instance.append(super().__new__(cls))
        return cls.__instance[-1]

    def __init__(self, name) -> None:
        self.name = name

objs = [SingletonFive(str(n)) for n in range(10)]

print(*[obj.name for obj in objs])