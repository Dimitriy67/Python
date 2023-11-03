# Реализуйте класс SuperString, описывающий строку.
# При создании экземпляра класс должен принимать один аргумент:
# string — значение строки
# Экземпляр класса SuperString должен иметь следующее неформальное строковое представление:
# <значение строки>
# Помимо этого, экземпляры класса SuperString должны поддерживать между собой операцию сложения
# с помощью оператора +, результатом которой должен являться новый экземпляр класса SuperString,
# представляющий конкатенацию исходных.
# Также экземпляр класса SuperString должен поддерживать операции умножения, деления,
# побитового сдвига влево и побитового сдвига вправо на целое число n с помощью операторов *, /, << и >>

class SuperString:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def __add__(self, other):
        if isinstance(other, SuperString):
            return SuperString(self.string + other.string)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return SuperString(self.string * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, int):
            return SuperString(self.string[:len(self.string) // other])
        return NotImplemented

    def __lshift__(self, other):
        if isinstance(other, int):
            if (length := len(self.string)) <= other:
                return SuperString('')
            else:
                return SuperString(self.string[0:length - other])
        return NotImplemented

    def __rshift__(self, other):
        if isinstance(other, int):
            if len(self.string) <= other:
                return SuperString('')
            else:
                return SuperString(self.string[other:])
        return NotImplemented