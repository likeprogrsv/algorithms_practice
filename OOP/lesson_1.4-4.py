
data = """tree - дерево
car - машина
car - автомобиль
leaf - лист
river - река
go - идти
go - ехать
go - ходить
milk - молоко"""



class Translator:
    dict = {}

    def add(self, eng, rus):
        # self.dict = {}
        if 'dict' not in self.__dict__:
            self.dict = {}

        self.dict.setdefault(eng, [])
        if rus not in self.dict[eng]: 
            self.dict[eng].append(rus)
        

    def remove(self, eng):
        self.dict.pop(eng, None)

    def translate(self, eng):
        return self.dict[eng]
        

tr = Translator()
[tr.add(eng, rus) for eng, rus in [s.split(' - ') for s in data.split('\n')]]
tr.remove('car')
print(*tr.translate('go'))
# print(tr.__dict__)
