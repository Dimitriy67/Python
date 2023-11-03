# Реализуйте функцию inversions(), которая принимает один аргумент:
# sequence — последовательность, элементами которой являются числа
# Функция должна возвращать единственное число — количество инверсий в последовательности sequence.

from itertools import combinations


def inversions(obj):
    return len(list(filter(lambda x: x[0] > x[1], combinations(obj, 2))))
