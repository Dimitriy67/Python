# Реализуйте функцию pluck(), которая принимает три аргумента в следующем порядке:
# data — словарь произвольной вложенности
# path — строка, представляющая собой ключ или последовательность ключей, перечисленных через точку .
# default — произвольный объект, значение по умолчанию; имеет значение None, если не передан явно
# Функция должна возвращать значение по ключу path из словаря data.
def pluck(data, path, default=None):
    path_list = path.split('.')
    search = data
    for i in path_list:
        search = search.get(i)
        if search is None:
            return default
    return search
