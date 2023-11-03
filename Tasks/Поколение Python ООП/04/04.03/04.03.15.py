# Реализуйте класс Knight, описывающий шахматного коня. При создании экземпляра класс должен принимать три аргумента в следующем порядке:
# horizontal — координата коня по горизонтальной оси, представленная латинской буквой от a до h
# vertical — координата коня по вертикальной оси, представленная целым числом от 1 до 8 включительно
# color — цвет коня (black или white)

class Knight:
    def __init__(self, horizontal, vertical, color):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color

    def get_char(self):
        return 'N'

    def can_move(self, horizontal, vertical):
        return (ord(self.horizontal) - ord(horizontal)) ** 2 + (self.vertical - vertical) ** 2 == 5

    def move_to(self, horizontal, vertical):
        if self.can_move(horizontal, vertical):
            self.horizontal = horizontal
            self.vertical = vertical

    def draw_board(self):
        for row in range(8, 0, -1):
            for column in 'abcdefgh':
                if self.horizontal == column and self.vertical == row:
                    print(self.get_char(), end='')
                elif self.can_move(column, row):
                    print('*', end='')
                else:
                    print('.', end='')
            print()
