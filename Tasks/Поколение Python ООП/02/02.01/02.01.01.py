# Будем считать, что игровое поле для игры в дартс представляет собой квадратную матрицу, 
# заполненную натуральными числами, расположенными в порядке возрастания от краев к центру. 
# Стороной игрового поля будем называть сторону квадратной матрицы, которую представляет это поле.
# Напишите программу, которая создает поле для игры в дартс определенного размерера

from math import ceil

n = int(input())
value_iteration = ceil(n / 2) - 1

matrix = [[1] * n for _ in range(n)]

start, end = 1, n - 2

for i in range(1, value_iteration + 1):
    for row in range(start, end + 1):
        for column in range(start, end + 1):
            matrix[row][column] = i + 1
    start, end = start + 1, end - 1

for i in matrix:
    print(*i)
