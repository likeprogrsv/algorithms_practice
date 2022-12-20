
from random import choice, sample


class Line:

    def __init__(self, a, b, c, d) -> None:       
        self.sp = (a, b,)
        self.ep = (c, d,)


class Rect:    
    def __init__(self, a, b, c, d) -> None:    
        self.sp = (a, b,)
        self.ep = (c, d,)


class Ellipse:
    def __init__(self, a, b, c, d) -> None:    
            self.sp = (a, b,)
            self.ep = (c, d,)
        


'''был мой вариант'''
# elements = []
# for _ in range(217):
#     a, b, c, d = (random.randint(0, 100) for x in range(4))
#     elements.append(random.choice([Line(a, b, c, d), Rect(a, b, c, d), Ellipse(a, b, c, d)]))

classes = (Line, Rect, Ellipse)
elements = [choice(classes)(*sample(range(100), 4)) for _ in range(217)]


for x in elements:
    if isinstance(x, Line):
        x.sp = x.ep = (0, 0,)


print(elements[3].__dict__)