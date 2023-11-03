# Реализуйте класс AnyClass. 
# При создании экземпляра класс должен принимать произвольное количество именованных аргументов и устанавливать их в качестве атрибутов создаваемому экземпляру.
# Экземпляр класса AnyClass должен иметь следующее формальное строковое представление:
# AnyClass(<имя 1-го атрибута>=<значение 1-го атрибута>, <имя 2-го атрибута>=<значение 2-го атрибута>, ...)
# И следующее неформальное строковое представление:
# AnyClass: <имя 1-го атрибута>=<значение 1-го атрибута>, <имя 2-го атрибута>=<значение 2-го атрибута>, ...

class AnyClass:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.attributes_str = ', '.join(
            f'{key}={repr(value)}' for key, value in self.__dict__.items())

    def __str__(self) -> str:
        return f'{self.__class__.__name__}: {self.attributes_str}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.attributes_str})'
