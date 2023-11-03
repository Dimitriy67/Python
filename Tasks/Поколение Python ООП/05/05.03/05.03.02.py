# Реализуйте класс Word, описывающий слово. При создании экземпляра класс должен принимать один аргумент:
# word — слово
# Экземпляр класса Word должен иметь следующее формальное строковое представление:
#Word('<слово в исходном виде>')
# И следующее неформальное строковое представление:
# <слово, в котором первая буква заглавная, а все остальные строчные>
# Также экземпляры класса Word должны поддерживать между собой все операции сравнения с помощью операторов ==, !=, >, <, >=, <=. 
# Два слова считаются равными, если их длины совпадают. 
# Слово считается больше другого слова, если его длина больше.

from functools import total_ordering


@total_ordering
class Word:
    def __init__(self, word) -> None:
        self.word = word

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.word}')"

    def __str__(self) -> str:
        return self.word.capitalize()

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Word):
            return len(self.word) == len(__value.word)
        return NotImplemented

    def __lt__(self, __value: object) -> bool:
        if isinstance(__value, Word):
            return len(self.word) < len(__value.word)
        return NotImplemented

