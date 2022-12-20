import sys

# здесь объявляются все необходимые классы

class ListObject:
    def __init__(self, data) -> None:
        self.data = data
        self.next_obj = None

    def link(self, obj):
        self.next_obj = obj


# считывание списка из входного потока (эту строку не менять)
lst_in = list(map(str.strip, sys.stdin.readlines())) # список lst_in в программе не менять

# здесь создаются объекты классов и вызываются нужные методы
head_obj = ListObject(lst_in[0])
obj = head_obj
for i in range(1, len(lst_in)):
    new_obj = ListObject(lst_in[i])
    obj.link(new_obj)
    obj = new_obj