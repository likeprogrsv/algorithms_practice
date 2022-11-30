class InfiniteExponentiation:

    def __init__(self, number, degree):
        self.number = number
        self.degree = degree

    def __next__(self):
        self.number = self.number ** self.degree
        return self.number

    def __iter__(self):
        return self


infinite_numbers = InfiniteExponentiation(4, 3)

print(next(infinite_numbers))
print(infinite_numbers.__next__())
# print(next(infinite_numbers))
# print(next(infinite_numbers))
# print(infinite_numbers.__iter__())
print(iter(infinite_numbers))