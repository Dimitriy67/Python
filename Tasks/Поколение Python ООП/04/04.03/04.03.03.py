# Реализуйте для класса House два метода экземпляра:
# paint() — метод, принимающий в качестве аргумента значение new_color и изменяющий текущий цвет дома на new_color
# add_rooms() — метод, принимающий в качестве аргумента целое число n и увеличивающий количество комнат в доме на n

class House:
    def __init__(self, color, rooms):
        self.color = color
        self.rooms = rooms

    def paint(self, new_color):
        self.color = new_color

    def add_rooms(self, new_rooms):
        self.rooms += new_rooms
