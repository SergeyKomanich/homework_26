from random import randint

# ЕСЛИ ПОЛЬЗОВАТЕЛЬ ВВЕЛ РАЗМЕР МАТРИЦЫ МЕНЬШЕ 5
while True:
    matrix_size = int(input('Введите число (размер матрицы), не меньше 5-ти: '))
    if matrix_size < 5:
        print('Вы ввели значение меньше 5-ти! Введите снова: ')
        continue
    else:
        break

# СОЗДАЕМ МАТРИЦУ
matrix = [[randint(1, 50) for i in range(matrix_size)] for j in range(matrix_size)]

# print(matrix)


def print_matrix(param):
    for i in range(matrix_size + 1):
        for j in range(matrix_size):
            print(f"{param[i][j] : > 4}", end="")
        print()


def sum_matrix_column(param):

    #  СЧИТАЕМ СУММЫ СТОЛБЦОВ И ДОБАВЛЯЕМ ИХ ЗНАЧЕНИЯ В МАСИВ
    sum_list = []

    for j in range(matrix_size):
        column_sum = 0
        for i in range(matrix_size):
            column_sum += param[i][j]
        sum_list.append(column_sum)
    param.append(sum_list)

    # ВЫВОД НЕОТСОРТИРОВАННОГО МАССИВА И СУММЫ СТОЛБЦОВ
    print('\n')
    print('Несортированный массив с суммами столбцов', end='\n')
    print()
    print_matrix(param)

    # СОРТИРУЕМ СТОЛБЦЫ ПО ВОЗРОСТАНИЮ СУММЫ
    for n in range(matrix_size - 1):
        for j in range(matrix_size - n - 1):
            if param[matrix_size][j] > param[matrix_size][j + 1]:
                param[matrix_size][j], param[matrix_size][j + 1] = \
                    param[matrix_size][j + 1], param[matrix_size][j]
                for i in range(matrix_size):
                    param[i][j], param[i][j + 1] = param[i][j + 1], param[i][j]

    # СОРТИРУЕМ ЭЛЕМЕНТЫ В СТОЛБЦАХ: В ЧЕТНЫХ ПО УБЫВАНИЮ, В НЕЧЕТНЫХ ПО ВОЗРОСТАНИЮ

    for j in range(matrix_size):
        if j % 2 == 0:
            for n in range(matrix_size - 1):
                for i in range(matrix_size - n - 1):
                    if param[i][j] < param[i + 1][j]:
                        param[i][j], param[i + 1][j] = param[i + 1][j], param[i][j]
        elif j % 2 > 0:
            for n in range(matrix_size - 1):
                for i in range(matrix_size - n - 1):
                    if param[i][j] > param[i + 1][j]:
                        param[i][j], param[i + 1][j] = param[i + 1][j], param[i][j]
    # ОТСОРТИРОВАННЫЙ МАССИВ
    print('\n')
    print('Отсортированный массив с суммами столбцов', end='\n')
    print()
    print_matrix(param)

# ВЫЗЫВАЕМ ФУНКЦМЮ СОРТИРОВКИ


sum_matrix_column(matrix)


























