class Meta(type):
       
    def __init__(cls, name, base, attrs):
        cls.class_attrs = attrs
        cls.__init__ = Meta.create_local_attrs

    def create_local_attrs(self, *args, **kwargs):
        for key, value in self.class_attrs.items():
            self.__dict__[key] = value



class Women(metaclass=Meta):
    title = 'afdfdfdf'
    content = 'fafddddq3'
    photo = 'gdgk laaalk'

class Man(metaclass=Meta):
    name = 'ffff'
    last_name = '22ewewe'
    photo = 'wwwwwwwwwwwwww'
    some = [2,1,1,3]


w = Women()
m = Man()
print(w.__dict__, m.__dict__, sep='\n')
