
nums = [10, -5, 100, 20, 0, 80, 45, 2, 5, 7]

class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data    

    def draw(self):
        print(*[self.data[i] for i in range(len(self.data)) if self.LIMIT_Y[0] <= self.data[i] <=self.LIMIT_Y[1]])

graph_1 = Graph()
graph_1.set_data(nums)
graph_1.draw()