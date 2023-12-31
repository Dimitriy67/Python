# Реализуйте класс Vector, описывающий вектор на плоскости. 
# При создании экземпляра класс должен принимать два аргумента в следующем порядке:
# x — координата вектора по оси x
#y — координата вектора по оси y
# Экземпляр класса Vector должен иметь следующее формальное строковое представление:
# Vector(<координата x>, <координата y>)
# И следующее неформальное строковое представление:
# Вектор на плоскости с координатами (<координата x>, <координата y>)

class Vector:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'Вектор на плоскости с координатами ({self.x}, {self.y})'

    def __repr__(self) -> str:
        return f'Vector({self.x}, {self.y})'


vectors = [Vector(1, 2), Vector(3, 4)]

print(vectors)
