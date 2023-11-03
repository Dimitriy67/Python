# Реализуйте класс Vector, описывающий вектор на плоскости.
# При создании экземпляра класс должен принимать два аргумента в следующем порядке:
# x — координата вектора по оси x
# y — координата вектора по оси y
# Экземпляр класса Vector должен иметь следующее формальное строковое представление:
# Vector(<координата x>, <координата y>)
# Также экземпляры класса Vector должны поддерживать между собой операции сложения и вычитания
# с помощью операторов + и - соответственно

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, n):
        if isinstance(n, (int, float)):
            return Vector(self.x * n, self.y * n)
        return NotImplemented

    def __rmul__(self, n):
        return self.__mul__(n)

    def __truediv__(self, n):
        if isinstance(n, (int, float)):
            return Vector(self.x / n, self.y / n)
        return NotImplemented

    def __rtruediv__(self, n):
        return self.__truediv__(n)

