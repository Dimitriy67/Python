# Реализуйте генераторную функцию intersperse(), которая принимает два аргумента в следующем порядке:
# iterable — итерируемый объект
# delimiter — значение-разделитель
# Функция должна возвращать генератор, порождающий последовательность из элементов итерируемого объекта iterable, между которыми располагается значение-разделитель delimiter.
def intersperse(iterable, delimiter):
    for key, value in enumerate(iterable):
        if key:
            yield delimiter
        yield value
