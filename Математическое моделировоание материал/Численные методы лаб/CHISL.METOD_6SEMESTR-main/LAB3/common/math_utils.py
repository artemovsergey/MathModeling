def copy_matrix(A):
    return [row[:] for row in A]

# нахождение определителя
# описание алгоритма https://integratedmlai.com/find-the-determinant-of-a-matrix-with-pure-python-without-numpy-or-scipy/
# рекурсивный алгоритм 1. закрываяем столбец и строку, находим определитель для маленьких матриц
def calc_determinant(A, total=0):
    # сохраняем индексы
    indices = list(range(len(A)))
     
    # если матрица 2 на 2
    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val
 
    # переходим к подматрицам
    for fc in indices:#"фокусирумеся"(закрываем) колонку fc
        As = copy_matrix(A)#копируем
        As = As[1:]#удаляем первую строку
        height = len(As) 
 
        for i in range(height): 
            # удаляем(закрваем) столбец
            As[i] = As[i][0:fc] + As[i][fc+1:] 
 
        sign = (-1) ** (fc % 2)#F
        # рекурсвивно вызываем для маленьких матриц
        sub_det = calc_determinant(As)
        # объединяем
        total += sign * A[0][fc] * sub_det 
 
    return total

# тесты результат должен быть равен -60
# https://ru.onlinemschool.com/math/assistance/matrix/determinant/
# print(determinant_recursive([
#     [1, 2, 3],
#     [4, 10, 6],
#     [7, 8, 9]
# ]))

# A матрица из коэффициентов системы
def solve_equation_system(A):
    without_last_column = []
    last_column = []
    for row_index in range(len(A)):
        row = []
        for column_index in range(len(A[row_index])):
            if column_index == len(A[row_index]) - 1:
                last_column.append(A[row_index][column_index])
                continue
            row.append(A[row_index][column_index])
        without_last_column.append(row)

    a_determinant = calc_determinant(without_last_column)

    results = []
    # c - индекс колонки, которой нужно заменить на последний столбец
    for c in range(len(without_last_column)):
        target_matrix = []
        for row_index in range(len(without_last_column)):
            row = []
            for column_index in range(len(without_last_column[row_index])):
                if column_index == c:
                    row.append(last_column[row_index])
                    continue
                row.append(without_last_column[row_index][column_index])
            target_matrix.append(row)
        results.append(calc_determinant(target_matrix) / a_determinant)
    return results