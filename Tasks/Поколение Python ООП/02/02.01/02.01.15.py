# Реализуйте декоратор @recviz, который полностью визуализирует выполнение декорируемой функции, в том числе и рекурсивной.
from functools import wraps


def recviz(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        indentation = "    " * wrapper.level
        print(f"{indentation}-> {func.__name__}({', '.join(map(repr, args))})")

        wrapper.level += 1
        result = func(*args, **kwargs)
        wrapper.level -= 1

        print(f"{indentation}<- {result}")
        return result

    wrapper.level = 0  # Инициализируем уровень рекурсии для каждой функции
    return wrapper
