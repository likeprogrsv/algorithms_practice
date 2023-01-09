class ShopInterface:
    __counter = 0

    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')
    
    @classmethod
    def set_id(cls):
        cls.__counter += 1
        return cls.__counter
    
class ShopItem(ShopInterface):
    def __init__(self, name, weight, price) -> None:
        self._name = name
        self._weight = self.__validate(weight)
        self._price = self.__validate(price)
        self.__id = self.set_id()

    def get_id(self):        
        return self.__id

    def __validate(self, value):
        if isinstance(value, (int, float)) and value > 0:
            return value
        else:
            raise TypeError('Должно быть положительное число')


item = ShopItem('phonee', 0.3, 25000)
item2 = ShopItem('e', 0.2, 24000)
item3 = ShopItem('qq', 0.33, 22000)



"""
class ShopInterface:

    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')
    
    def set_id(self):
        return hash(self)
    
class ShopItem(ShopInterface):
    def __init__(self, name, weight, price) -> None:
        self._name = name
        self._weight = self.__validate(weight)
        self._price = self.__validate(price)
        self.__id = self.set_id()

    def get_id(self):        
        return self.__id

    def __validate(self, value):
        if isinstance(value, (int, float)) and value > 0:
            return value
        else:
            raise TypeError('Должно быть положительное число')



"""