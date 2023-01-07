class PriceValue:
    def __init__(self, max_value) -> None:
        self.max_value = max_value

    def validate(self, value):
        if type(value) not in (float, int) or value not in range(0, self.max_value + 1):
            return False  
        return True

    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if self.validate(value):
            instance.__dict__[self.name] = value


class StringValue:
    def __init__(self, min_length, max_length) -> None:
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, value):
        if type(value) is not str or len(value) not in range(self.min_length, self.max_length + 1):
            return False 
        return True

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.validate(value):
            instance.__dict__[self.name] = value



class Product:
    name = StringValue(2, 50)
    price = PriceValue(10000)

    def __init__(self, product_name, product_price) -> None:
        self.name = product_name
        self.price = product_price
    


class SuperShop:
    def __init__(self, name) -> None:
        self.name = name
        self.goods = []
    
    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.pop()


shop = SuperShop("У Балакирева")
t = Product("Курс по Python", 0)
shop.add_product(t)
shop.add_product(Product("Курс по Python ООП", 2000))
for p in shop.goods:
    print(f"{p.name}: {p.price}")
t1 = Product(1000, "name 123")
shop.add_product(t1)

shop.remove_product(t)