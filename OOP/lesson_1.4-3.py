import sys

# программу не менять, только добавить два метода
# lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
lst_in = ["1 Сергей 35 120000",
        "2 Федор 23 12000",
        "3 Иван 13 1200"]

class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    # здесь добавлять методы
    def insert(self, data):
        
        for line in data:  
            self.dict = {}  
            for k, v in zip(self.FIELDS, line.split(' ')):
                self.dict[k] = v
            self.lst_data.append(self.dict)

    def select(self, a, b):
        if b in range(0, (len(self.lst_data) + 1)):
            return self.lst_data[a:b]
        else: return f'Диапазон за границами списка'
db = DataBase()
db.insert(lst_in)
print(db.select(1, 3))
# s = 'adasfaf adasf'
# s.split(' ')