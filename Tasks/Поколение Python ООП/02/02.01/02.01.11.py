# Реализуйте функцию is_fraction(), которая принимает один аргумент:
# string — строка, содержащая произвольный набор символов
# Функция должна возвращать True, если строка string представляет собой обыкновенную дробь, или False в противном случае.
from re import fullmatch


def is_fraction(s):
    pattern = r'^-?\d+/\d*[1-9]\d*$'
    find = fullmatch(pattern, s)
    return bool(find)
