# Реализуйте класс FoodInfo, описывающий пищевую ценность продуктов.
# При создании экземпляра класс должен принимать три аргумента в следующем порядке:
# proteins — количество белков в граммах
# fats — количество жиров в граммах
# carbohydrates — количество углеводов в граммах
# Экземпляр класса FoodInfo должен иметь три атрибута:
# proteins — количество белков в граммах
# fats — количество жиров в граммах
# carbohydrates — количество углеводов в граммах
# И следующее формальное строковое представление:
# FoodInfo(<количество белков>, <количество жиров>, <количество углеводов>)
# Также экземпляры класса FoodInfo должны поддерживать между собой операцию сложения с помощью оператора +,
# результатом которой должен являться новый экземпляр класса FoodInfo с суммарным количеством белков,
# жиров и углеводов исходных экземпляров.
# Наконец, экземпляр класса FoodInfo должен поддерживать операции умножения, деления и деления нацело
# на число n с помощью операторов *, / и //

class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def __repr__(self):
        return f'FoodInfo({self.proteins}, {self.fats}, {self.carbohydrates})'

    def __add__(self, other):
        if isinstance(other, FoodInfo):
            return FoodInfo(self.proteins + other.proteins,
                            self.fats + other.fats,
                            self.carbohydrates + other.carbohydrates)
        return NotImplemented

    def __mul__(self, n):
        if isinstance(n, (int, float)):
            return FoodInfo(self.proteins * n, self.fats * n, self.carbohydrates * n)
        return NotImplemented

    def __rmul__(self, n):
        return self.__mul__(n)

    def __truediv__(self, n):
        if isinstance(n, (int, float)):
            return FoodInfo(self.proteins / n, self.fats / n, self.carbohydrates / n)
        return NotImplemented

    def __rtruediv__(self, n):
        return self.__truediv__(n)

    def __floordiv__(self, n):
        if isinstance(n, (int, float)):
            return FoodInfo(self.proteins // n, self.fats // n, self.carbohydrates // n)
        return NotImplemented

    def __rfloordiv__(self, n):
        return self.__floordiv__(n)

