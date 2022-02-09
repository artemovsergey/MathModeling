const { generate_square_matrix, print_matrix, extract_square_matrix_from, generate_vector, extract_last_column_from } = require("./utils")

function use_lu(matrix) {
    console.log('===================ИСПОЛЬЗУЯ LU РАЗЛОЖЕНИЕ============================')
    const A = extract_square_matrix_from(matrix)
    const C = generate_square_matrix(A.length)
    const B = generate_square_matrix(A.length)

    const d = extract_last_column_from(matrix)

    for (let i = 0; i < A.length; i++) {
            C[i][i] = 1
    }

    for (let i = 0; i < A.length; i++) {
        for (let j = 0; j < A[i].length; j++) {
            if (i >= j) {
                if (j === 0) {
                    B[i][0] = A[i][0]
                } else {
                    let sum = 0;
                    for (let k = 0; k < j; k++) {
                        sum += B[i][k] * C[k][j]
                    }
                    B[i][j] = A[i][j] - sum;
                }

            } else if (i < j) {
                if (i === 0) {
                    C[0][j] = A[0][j] / B[0][0]
                } else {
                    let sum = 0;
                    for (let k = 0; k < i; k++) {
                        sum += B[i][k]* C[k][j]
                    }
                    C[i][j] = (1 / B[i][i])  * ( A[i][j] - sum)
                }
            }

        }
    }

    console.log('МАТРИЦЫ U и L')
    print_matrix(C)
    print_matrix(B)

    let y_vector = generate_vector(C.length)

    for (let i = 0; i < matrix.length; i++) {
        if (i === 0) {
            y_vector[0] = d[0] / B[0][0]
        } else {
            let sum  = 0;
            for (let k = 0; k <= i - 1; k++) {
                sum += B[i][k] * y_vector[k]
            }
            y_vector[i] = (1 / B[i][i]) * (d[i] - sum)
        }
    }

    let x_vector = generate_vector(C.length)

    x_vector[C.length - 1] = y_vector[C.length - 1]
    for (let i = C.length - 2; i >= 0; i--) {
        let sum = 0;
        for (let k = i + 1; k < C.length; k++) {
            sum += C[i][k] * x_vector[k]
        }
        x_vector[i] = y_vector[i] - sum;
    }

    console.log('вектор X')
    console.log(y_vector)
    console.log('вектор Y')
    console.log(x_vector);

}

module.exports = {
    use_lu,
}

// 1.00  2.00  0.00  -6.50  -3.50
// 0.00  0.00  0.00  -7.50  -7.50
// 0.00  0.00  1.00  3.50  4.50
// 0.00  0.00  0.00  0.00  0.00