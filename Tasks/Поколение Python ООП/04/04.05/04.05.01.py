# Реализуйте класс Rectangle, описывающий прямоугольник.
# При создании экземпляра класс должен принимать два аргумента в следующем порядке:
# length — длина прямоугольника
# width — ширина прямоугольника
# Экземпляр класса Rectangle должен иметь два атрибута:
# length — длина прямоугольника
# width — ширина прямоугольника
# Класс Rectangle должен иметь два свойства:
# perimeter — свойство, доступное только для чтения, возвращающее периметр прямоугольника
# area — свойство, доступное только для чтения, возвращающее площадь прямоугольника

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2*(self.length + self.width)

    def area(self):
        return self.length * self.width

    perimeter = property(perimeter)
    area = property(area)
