class Clock:
    def __init__(self, time):
        self.__time = time if self.__check_time(time) else 0

    @classmethod
    def __check_time(cls, tm):
        return type(tm) == int and 0 <= tm < 100000

    def set_time(self, tm):        
        self.__time = tm if self.__check_time(tm) else self.__time
    
    def get_time(self):
        return self.__time

    
clock = Clock(4530)
