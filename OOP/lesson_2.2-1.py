class Car:
    def __init__(self) -> None:
        self.__model = ''

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, name):
        self.__model = name if type(name) is str and len(name) in range(2, 101) else self.__model


car = Car()
car.model = 'Toyota'
print(car.model)