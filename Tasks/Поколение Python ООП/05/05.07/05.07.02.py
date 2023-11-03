# Реализуйте класс Temperature, описывающий температуру в градусах по шкале Цельсия.
# При создании экземпляра класс должен принимать один аргумент:
# temperature — температура в градусах по шкале Цельсия
# Класс Temperature должен иметь один метод экземпляра:
# to_fahrenheit() — метод, возвращающий температуру по шкале Фаренгейта
# Класс Temperature должен иметь один метод класса:
# from_fahrenheit() — метод, принимающий в качестве аргумента температуру по шкале Фаренгейта
# и возвращающий экземпляр класса Temperature, созданный на основе переданной температуры

class Temperature:
    def __init__(self, temperature):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 9 / 5) + 32

    @classmethod
    def from_fahrenheit(cls, temp):
        return cls((temp - 32) * 5/9)

    def __str__(self):
        return f'{round(self.temperature, 2)}°C'

    def __bool__(self):
        return self.temperature > 0

    def __int__(self):
        return int(self.temperature)

    def __float__(self):
        return float(self.temperature)


