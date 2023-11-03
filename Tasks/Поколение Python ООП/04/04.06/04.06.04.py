# Реализуйте класс Color, описывающий цвет. При создании экземпляра класс должен принимать один аргумент:
# hexcode — шестнадцатеричное значение цвета
# Экземпляр класса Color должен иметь три атрибута:
# r — интенсивность красного компонента цвета в виде десятичного числа
# g — интенсивность зеленого компонента цвета в виде десятичного числа
# b — интенсивность синего компонента цвета в виде десятичного числа
# Класс Color должен иметь одно свойство:
# hexcode — свойство, доступное для чтения и записи, возвращающее шестнадцатеричное значение цвета

class Color:
    def __init__(self, hexcode):
        self.hexcode = hexcode

    @property
    def hexcode(self):
        return self._hexcode

    @hexcode.setter
    def hexcode(self, hexcode):
        self._hexcode = hexcode.upper()
        self.r = int(hexcode.upper()[:2], 16)
        self.g = int(hexcode.upper()[2:4], 16)
        self.b = int(hexcode.upper()[-2:], 16)
