# Реализуйте класс Circle, описывающий круг. При создании экземпляра класс должен принимать один аргумент:
# radius — радиус круга
# Экземпляр класса Circle должен иметь три атрибута:
# _radius — радиус круга
# _diameter — диаметр круга
# _area — площадь круга

from math import pi


class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._diameter = radius * 2
        self._area = pi * radius**2

    def get_radius(self):
        return self._radius

    def get_diameter(self):
        return self._diameter

    def get_area(self):
        return self._area
