# Будем считать атрибут защищенным, если его имя начинается с символа нижнего подчеркивания (_).
# Например, _password, __email и __dict__.
# Реализуйте класс ProtectedObject.
# При создании экземпляра класс должен принимать произвольное количество именованных аргументов.
# Все передаваемые аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов.
# Класс ProtectedObject должен запрещать получать и изменять значения защищенных атрибутов своих экземпляров,
# а также удалять эти атрибуты. При попытке получить или изменить значение защищенного атрибута,
# а также попытке удалить атрибут, должно возбуждаться исключение AttributeError с текстом:
# Доступ к защищенному атрибуту невозможен

class ProtectedObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            object.__setattr__(self, key, value)

    def __setattr__(self, key, value):
        if key.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        object.__setattr__(self, key, value)

    def __getattribute__(self, item):
        if item.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        return object.__getattribute__(self, item)

    def __delattr__(self, item):
        if item.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        object.__delattr__(self, item)

