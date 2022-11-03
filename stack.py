from collections import deque


# Реализовать queue с использованием двух Stackов
class Queue:

    # 1ТП4Т Конструктор
    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()

    # Добавить элемент в queue
    def enqueue(self, data):

        # Переместить все элементы из первого stack во второй стек
        while len(self.s1):
            self.s2.append(self.s1.pop())

        # поместить элемент в первый stack
        self.s1.append(data)

        # Переместить все элементы обратно в первый стек из второго stack
        while len(self.s2):
            self.s1.append(self.s2.pop())

    # Удалить элемент из queue
    def dequeue(self):

        # , если первый stack пуст
        if not self.s1:
            print('Underflow!!')
            exit(0)

        # возвращает верхний элемент из первого stack
        return self.s1.pop()


if __name__ == '__main__':

    keys = [1, 2, 3, 4, 5]
    q = Queue()

    # вставить выше ключи
    for key in keys:
        q.enqueue(key)

    print(q.dequeue())  # 1
    print(q.dequeue())  # 2