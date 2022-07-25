# Завдання 4 (додаткове)
# Файл: spiral.py Оцінка: 25
# Створіть функцію def spiral(matrix) яка приймає цілочисельну матрицю розміром NxM та повертає масив в якому числа з матриці записані в порядку спіралі. Матриця виглядає наступним чином:
# [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# Це масив цілочисельних масивів. Наприклад матриця розміром 3x4 виглядає ось так:
# [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# Тестувати функцію ви можете як завгодно: за допомогою модуля sys і аргументів програми, або за допомогою input() або в результаті викликів функції. Але в файлі spiral.py повина бути створена функція def spiral(matrix) яка виконує необхідну логіку.
# Приклади:
# spiral([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) -> [1, 2, 3, 6, 9, 8, 7, 4, 5]
# spiral([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) -> [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

import sys


def spiral(matrix):
    if not matrix_is_int(matrix):
        print("Value error")
        sys.exit()

    list = []
    start_row = 0
    start_column = 0
    end_row = len(matrix)
    end_column = len(matrix[0])
    while (start_row < end_row and start_column < end_column):
        for el in range(start_column, end_column):
            list.append(matrix[start_row][el])
        start_row += 1
        for el in range(start_row, end_row):
            list.append(matrix[el][end_column-1])
        end_column -= 1
        if (start_row < end_row):
            for el in range(end_column-1, start_column-1, -1):
                list.append(matrix[end_row-1][el])
            end_row -= 1
        if (start_column < end_column):
            for el in range(end_row-1, start_row-1, -1):
                list.append(matrix[el][start_column])
            start_column += 1
    print(list)


def matrix_is_int(matrix):
    for row in matrix:
        for column in row:
            if type(column) != int:
                return False
    return True


spiral([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # -> [1,2,3,6,9,8,7,4,5]
# -> [1,2,3,4,8,12,11,10,9,5,6,7]
spiral([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
