# Реализуйте класс NonNegativeObject.
# При создании экземпляра класс должен принимать произвольное количество именованных аргументов.
# Все передаваемые аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов,
# причем если значением атрибута является отрицательное число, оно должно быть взято с противоположным знаком.

class NonNegativeObject:
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

    def __setattr__(self, name, value):
        if isinstance(value, (int, float)):
            value = abs(value)
        object.__setattr__(self, name, value)


