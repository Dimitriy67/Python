# Вам доступен класс Rectangle, описывающий прямоугольник. 
# При создании экземпляра класс принимает два аргумента в следующем порядке:
# length — длина прямоугольника
# width — ширина прямоугольника
# Реализуйте для экземпляров класса Rectangle следующее формальное и неформальное строковое представление:
# Rectangle(<длина прямоугольника>, <ширина прямоугольника>)

class Rectangle:
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width

    def __repr__(self) -> str:
        return f'Rectangle({self.length}, {self.width})'