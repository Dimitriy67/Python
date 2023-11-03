# Требовалось реализовать класс Item, описывающий предмет.
# При создании экземпляра класс должен был принимать три аргумента в следующем порядке:
# name — название предмета
# price — цена предмета в рублях
# quantity — количество предметов
# Предполагалось, что при обращении к атрибуту name экземпляра класса Item будет возвращаться его название с заглавной буквы,
# а при обращении к атрибуту total — произведение цены предмета на его количество.
# Программист торопился и решил задачу неправильно. Дополните приведенный ниже код и реализуйте правильный класс Item.

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __getattribute__(self, name):
        obj = object.__getattribute__(self, name)
        if name == 'name':
            return obj.title()
        return obj

    def __getattr__(self, item):
        if item == 'total':
            return self.price * self.quantity
        raise AttributeError


