# Реализуйте класс DevelopmentTeam, описывающий команду разработчиков двух уровней: junior (младший) и senior (старший).
# При создании экземпляра класс не должен принимать никаких аргументов.
# Класс DevelopmentTeam должен иметь два метода экземпляра:
# add_junior() — метод, принимающий произвольное количество позиционных аргументов,
# каждый из которых является именем разработчика, и добавляющий их в число junior-разработчиков
# add_senior() — метод, принимающий произвольное количество позиционных аргументов,
# каждый из которых является именем разработчика, и добавляющий их в число senior-разработчиков
# Экземпляр класса DevelopmentTeam должен быть итерируемым объектом, элементами которого сперва являются все его junior-разработчики,
# а затем — все senior-разработчики.
# Junior-разработчики должны быть представлены в виде кортежей:
# (<имя разработчика>, 'junior')
# в то время как senior-разработчики — в виде кортежей:
# (<имя разработчика>, 'senior')

class DevelopmentTeam:
    def __init__(self):
        self.jun_list = list()
        self.sen_list = list()

    def add_junior(self, *juniors):
        self.jun_list.extend(juniors)

    def add_senior(self, *seniors):
        self.sen_list.extend(seniors)

    def __iter__(self):
        for j in self.jun_list:
            yield j, 'junior'

        for s in self.sen_list:
            yield s, 'senior'
