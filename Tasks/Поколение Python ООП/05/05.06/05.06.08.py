# Реализуйте декоратор @CountCalls, который считает количество вызовов декорируемой функции.
# Счетчик вызовов должен быть доступен по атрибуту calls.
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        return self.func(*args, **kwargs)

