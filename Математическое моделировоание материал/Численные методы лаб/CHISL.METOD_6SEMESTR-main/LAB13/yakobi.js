const matrix = [
     [10, 1, 1, 12],
     [2, 10, 1, 13],
     [2, 2, 10, 14]
 ]

const { extract_last_column_from, generate_vector } = require("./utils");

//const matrix = [
//    [3.8, 1.1, -2.3, 4.8],
//    [-2.1, 8.9, -2.8, 3.3],
//    [1.8, 1.1, -4.1, 5.8]
//]
yakobi(matrix)

function check_diagonal_superiorment(matrix) {
    for (let i = 0; i < matrix.length; i++) {
        let sum = 0;
        for (let j = 0;j < matrix[i].length; j++) {
            if (i !== j) {
                sum += Math.abs(matrix[i][j])
            }
        }

        if (Math.abs(matrix[i][i]) > sum) {
            console.log('НЕТ ДИАГОНАЛЬНОГО ПРЕОБЛАДАНИЯ')
            return false;
        } else {
            return true;
        }
    }
}

function yakobi(matrix) {
    if (!check_diagonal_superiorment(matrix)) {
        return;
    }

    const EPS = 0.1;
    const F = extract_last_column_from(matrix)
    let X = generate_vector(matrix.length)
    let temp_x = generate_vector(matrix.length)
    let norm;
    let count = 0
    do {
        for (let i = 0; i < matrix.length; i++) {
            temp_x[i] = F[i]
            for (let g = 0; g < matrix.length; g++) {
                if (i !== g) {//диагональные элементы не учитываем
                    temp_x[i] -= matrix[i][g] * X[g]
                }
            }
            temp_x[i] /= matrix[i][i]//делимся на значения диагонали
        }
        norm = Math.abs(X[0] - temp_x[0]);//высчитываем норму(разницу последних итераций)

        for (let h = 0; h < matrix.length; h++) {
            if (Math.abs(X[h] - temp_x[h]) > norm) {//находим макс норму
                norm = Math.abs(X[h] - temp_x[h])
            }
            X[h] = temp_x[h]
        }
        count += 1
    } while(norm > EPS)//если норма стала меньше, чем целевая погрешность прекращаем итерации
    console.log(X)
    console.log(count+1)
}