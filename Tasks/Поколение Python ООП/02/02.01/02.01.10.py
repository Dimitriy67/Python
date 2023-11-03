# Реализуйте функцию is_decimal(), которая принимает один аргумент:
# string — строка, содержащая произвольный набор символов
# Функция должна возвращать True, если строка string представляет собой целое или вещественное число, или False в противном случае.
from re import fullmatch


def is_decimal(s):
    pattern = r'^-?(\d+(\.\d*)?|\.\d+)$'
    find = fullmatch(pattern, s)
    return bool(find)