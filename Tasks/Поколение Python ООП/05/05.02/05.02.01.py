#Исправьте приведенный ниже код и реализуйте класс Book правильно.
# Предполагалось, что экземпляры класса Book будут иметь следующее формальное строковое представление:
# Book('<название книги>', '<автор книги>', <год выпуска книги>)
# И следующее неформальное строковое представление:
# <название книги> (<автор книги>, <год выпуска книги>)

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f'{self.title} ({self.author}, {self.year})'

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

