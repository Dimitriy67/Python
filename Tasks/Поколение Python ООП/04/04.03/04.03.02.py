# Класс User имеет один метод экземпляра:
# add_friends() — метод, принимающий в качестве аргумента целое число n и увеличивающий количество друзей пользователя на n
# Найдите и исправьте ошибки, допущенные при реализации метода add_friends()

class User:
    def __init__(self, name, friends=0):
        self.name = name
        self.friends = friends

    def add_friends(self, n):
        self.friends += n
