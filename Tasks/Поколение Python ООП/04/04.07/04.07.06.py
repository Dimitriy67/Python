# Реализуйте класс CaseHelper, описывающий набор функций для работы со строками в стилях Snake Case и Upper Camel Case

from re import compile, sub


class CaseHelper:
    _SC = compile(r'^[a-z][a-z_]+[a-z0-9_]*$')
    _UPC = compile(r'^[A-Z][a-zA-Z0-9]*$')

    @staticmethod
    def is_snake(s):
        search = CaseHelper._SC.match(s)
        return bool(search)

    @staticmethod
    def is_upper_camel(s):
        search = CaseHelper._UPC.match(s)
        return bool(search)

    @staticmethod
    def to_snake(s):
        return sub(r'(?<!^)(?=[A-Z])', '_', s).lower()

    @staticmethod
    def to_upper_camel(s):
        return ''.join(word.title() for word in s.split('_'))
