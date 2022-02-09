 const matrix = [
     [10, 1, 1, 12],
     [2, 10, 1, 13],
     [2, 2, 10, 14]
 ]

const { extract_last_column_from, generate_vector } = require("./utils");

//const matrix = [
//    [115, -20, -75, 20],
//    [15, -50, -5, -40],
//    [6, 2, 20, 28]
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
    let count = 0
    const EPS = 0.01;
    const F = extract_last_column_from(matrix)
    let X = generate_vector(matrix.length)
    let temp_x = generate_vector(matrix.length)
    let norm;
    do {
        for (let i = 0; i < matrix.length; i++) {   //внешняя
            temp_x[i] = F[i]
            for (let g = 0; g < matrix.length; g++) {
                if (i !== g) {
                    //отличие от якоби
                    if (i > g) {//если у нас уже есть рассчитанные значения для иксов на текущей внешней итерации
                        temp_x[i] -= matrix[i][g] * temp_x[g]//то мы их используем
                    } else {
                        temp_x[i] -= matrix[i][g] * X[g]//если нет рассчитанных значений, то используем значения из предыдущих итераций
                    }
                }
            }
            temp_x[i] /= matrix[i][i]
        }
        norm = Math.abs(X[0] - temp_x[0]);
        for (let h = 0; h < matrix.length; h++) {
            if (Math.abs(X[h] - temp_x[h]) > norm) {
                norm = Math.abs(X[h] - temp_x[h])
            }
            X[h] = temp_x[h]
        }
        count += 1
    } while(norm > EPS)
    console.log(X)
    console.log(count)
}