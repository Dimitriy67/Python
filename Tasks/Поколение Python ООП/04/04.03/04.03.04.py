# Реализуйте класс Circle, описывающий круг. При создании экземпляра класс должен принимать один аргумент:
# radius — радиус круга
# Экземпляр класса Circle должен иметь три атрибута:
# radius — радиус круга
# diameter — диаметр круга
# area — площадь круга

from math import pi


class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius
        self.diameter = radius * 2
        self.area = pi * radius**2
