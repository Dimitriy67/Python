# Реализуйте класс Person, описывающий человека. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
# name — имя человека
# surname — фамилия человека
# Экземпляр класса Person должен иметь два атрибута:
# name — имя человека
# surname — фамилия человека
# Класс Person должен иметь одно свойство:
# fullname — свойство, доступное для чтения и записи, возвращающее полное имя человека в виде строки:
# <имя> <фамилия>

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_fullname(self):
        return f"{self.name} {self.surname}"

    def set_fullname(self, fullname):
        self.name, self.surname = fullname.split()

    fullname = property(get_fullname, set_fullname)
