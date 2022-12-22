class ObjList:

    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.__data = data

    def set_next(self, obj):
        """изменение приватного свойства __next на значение obj"""

        self.__next = obj
    
    def set_prev(self, obj):
        """изменение приватного свойства __prev на значение obj"""

        self.__prev = obj        
    
    def get_next(self):
        """получение значения приватного свойства __next;
        """
        return self.__next

    def get_prev(self):
        """получение значения приватного свойства __prev;
        """
        return self.__prev
    
    def set_data(self, data):
        """изменение приватного свойства __data на значение data;
        """
        self.__data = data
    
    def get_data(self):
        """получение значения приватного свойства __data.
        """
        return self.__data


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.obj = None

    def add_obj(self, new_obj):
        self.head = new_obj if self.head is None else self.head
        self.obj = new_obj if self.obj is None else self.obj
        self.tail = new_obj
        if self.head != self.tail:
            self.obj.set_next(new_obj)
            new_obj.set_prev(self.obj)
            self.obj = new_obj

    def remove_obj(self):        
        if self.tail.get_prev() is not None:
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)
            self.obj = self.tail
        else: self.head = self.obj = self.tail = None

    def get_data(self):
        obj = self.head
        data = []
        while obj is not None:
            data.append(obj.get_data())
            obj = obj.get_next()
        return data


lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
# lst.add_obj(ObjList("данные 2"))
# lst.add_obj(ObjList("данные 3"))
lst.remove_obj()
res = lst.get_data()    # ['данные 1', 'данные 2', 'данные 3']
print(res)

# print(lst)