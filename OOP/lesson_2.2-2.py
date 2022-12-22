class StackObj:
    def __init__(self, data) -> None:
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data 

    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, obj):
        self.__next = obj


class Stack:
    def __init__(self) -> None:
        self.top = None
        self.last = None

    def push(self, obj):
        self.top = obj if self.top is None else self.top
        if self.last is None:
            self.last = obj  
        else:        
            self.last.next = obj
            self.last = obj
        
    def pop(self):
        obj = self.top
        if obj is None:
            return 
        while obj and obj.next != self.last:
            obj = obj.next
        last = self.last
        self.last = obj
        if obj:
            obj.next = None
        if self.last is None:
            self.top = None
        return last

    def get_data(self):
        data = []
        obj = self.top
        while obj:
            data.append(obj.data)
            obj = obj.next
        return data


s = Stack()
top = StackObj("obj_1")
s.push(top)
# s.push(StackObj("obj_2"))
# s.push(StackObj("obj_3"))
s.pop()

res = s.get_data()
print(res)