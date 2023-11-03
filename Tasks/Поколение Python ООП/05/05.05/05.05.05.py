# Реализуйте класс Queue, описывающий очередь.
# При создании экземпляра класс должен принимать произвольное количество позиционных аргументов,
# каждый из которых является элементом очереди.
# Порядок следования аргументов образует порядок элементов в очереди,
# то есть первый аргумент — первый элемент очереди, второй аргумент — второй элемент очереди, и так далее.
# Класс Queue должен иметь два метода экземпляра:
# add() — метод, принимающий произвольное количество позиционных аргументов и добавляющий их в конец очереди в том порядке,
# в котором они были переданы
# pop() — метод, удаляющий из очереди первый элемент и возвращающий его.
# Если очередь пуста, метод должен вернуть значение None

class Queue:
    def __init__(self, *args):
        self.my_queue = list(args)

    def __str__(self):
        return ' -> '.join(str(i) for i in self.my_queue)

    def add(self, *args):
        self.my_queue.extend(args)

    def pop(self):
        return self.my_queue.pop(0) if self.my_queue else None

    def __eq__(self, other):
        return isinstance(other, Queue) and self.my_queue == other.my_queue

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        if isinstance(other, Queue):
            return Queue(*(self.my_queue + other.my_queue))
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Queue):
            self.my_queue += other.my_queue
            return self
        return NotImplemented

    def __rshift__(self, n):
        if isinstance(n, int):
            return Queue(*self.my_queue[n:])
        return NotImplemented
