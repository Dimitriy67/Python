# Реализуйте класс AttrsNumberObject.
# При создании экземпляра класс должен принимать произвольное количество именованных аргументов.
# Все передаваемые аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов.
# Экземпляр класса AttrsNumberObject должен иметь один атрибут:
# attrs_num — количество атрибутов, которыми обладает экземпляр класса AttrsNumberObject на данный момент,
# включая сам атрибут attrs_num

class AttrsNumberObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    @property
    def attrs_num(self):
        return len(self.__dict__) + 1

