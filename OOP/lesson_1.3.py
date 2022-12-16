class Figure:
    type_fig = 'ellipse'
    color = 'red'

    def __init__(self, start_pt, end_pt, color) -> None:
        self.start_pt = start_pt
        self.end_pt = end_pt
        self.color = color


fig1 = Figure((10, 5), (100, 20), 'blue')
delattr(fig1, 'color')
print(*fig1.__dict__)