import sys

class StreamData:

    def create(self, fields, lst_values):
        if len(fields) == len(lst_values):
            try:
                [setattr(self, fields[v], k) for v, k in enumerate(lst_values)]
                return True
            except:
                return False
        else: return False
    

class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res

sr = StreamReader()
data, result = sr.readlines()
