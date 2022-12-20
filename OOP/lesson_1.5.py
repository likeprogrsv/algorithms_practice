
class Point:

    def __init__(self, x, y, color='black') -> None:
        self.x = x
        self.y = y
        self.color = color
    

# points = [Point(x , x) for x in range(1, 2000) if x % 2 != 0]
# setattr(points[1], 'color', 'yellow')

points = [Point(x , x) for x in range(1, 2000, 2)]
points[1].color = 'yellow'
print(len(points))