const { extract_square_matrix_from, generate_square_matrix, extract_last_column_from, print_matrix } = require("./utils")

function find_determinant(matrix) {
    const A = extract_square_matrix_from(matrix)
    const B = generate_square_matrix(A.length)
    const C = generate_square_matrix(A.length)
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
    
    console.log('L')
    print_matrix(B)
    console.log('U')
    print_matrix(C)

    let result = 1;
    for (let i = 0; i < C.length; i++) {
        result *= B[i][i]
    }
    console.log('detA =', result)
}
module.exports = {
    find_determinant
}