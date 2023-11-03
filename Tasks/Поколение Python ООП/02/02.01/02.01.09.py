# Реализуйте функцию is_integer(), которая принимает один аргумент:
# string — строка, содержащая произвольный набор символов
# Функция должна возвращать True, если строка string представляет собой целое число, или False в противном случае.
from re import fullmatch


def is_integer(s):
    pattern = r'-?\d+'
    find = fullmatch(pattern, s)
    return bool(find)
