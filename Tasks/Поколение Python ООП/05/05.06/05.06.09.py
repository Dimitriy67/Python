# Реализуйте декоратор @CachedFunction, который кэширует вычисленные значения декорируемой функции.
# Кэш должен быть доступен по атрибуту cache и представлять собой словарь,
# ключом в котором является кортеж с аргументами, а значением — возвращаемое значение декорируемой функции
# при вызове с этими аргументами.

class CachedFunction:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]



