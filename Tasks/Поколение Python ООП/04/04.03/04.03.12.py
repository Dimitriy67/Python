# Реализуйте класс Todo, описывающий список дел. При создании экземпляра класс не должен принимать никаких аргументов.

class Todo:
    def __init__(self):
        self.things = []

    def add(self, business, priority):
        self.things.append((business, priority))
        self.min_priority = min(p for _, p in self.things)
        self.max_priority = max(p for _, p in self.things)

    def get_by_priority(self, n):
        return [b for b, p in self.things if p == n]

    def get_low_priority(self):
        return [b for b, p in self.things if p == self.min_priority]

    def get_high_priority(self):
        return [b for b, p in self.things if p == self.max_priority]
