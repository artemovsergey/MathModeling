const { generate_vector, clone, generate_matrix, generate_square_matrix, extract_last_column_from } = require("./utils")

 const matrix = [
     [6.25, -1, 0.5, 7.5],
     [-1, 5, 2.12, -8.68],
     [0.5, 2.12, 3.6, -0.24]
 ]
// const matrix = [
//     [3.42, -1.15, 1.07, 2.48],
//     [-1.15, 3.76, -1.18, 1.15],
//     [1.07, -1.18, 2.23, 0.88]
// ]
//const matrix = [
//  [2.5, -0.9, 0.2, -0.7],
//  [-0.9, 3.8, -0.1, 2.5],
//  [0.2, -0.1, 0.9, 0.1]
//]

relax_with(matrix)

function relax_with(matrix) {
    let X = generate_vector(matrix.length)
    const F = extract_last_column_from(matrix)
    const w = 1.2;
    const eps = 0.001
    const b = generate_square_matrix(matrix.length)
    const c = generate_vector(matrix.length)
    let count = 0
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0;j < matrix.length; j++) {
            if (i === j) {
                b[i][j] = 0
            } else {
                b[i][j] = - matrix[i][j] / matrix[i][i]
            }
        }
    }
    for (let i = 0;i < matrix.length; i++) {
        c[i] = F[i] / matrix[i][i]
    }
    while (true) {
        count += 1
        let new_x = clone(X)
        for (let i = 0;i < b.length; i++) {
            let left_sum = 0;
            for (let j = 0; j < i; j++) {
                left_sum += b[i][j] *  new_x[j]
            }
            let right_sum = 0;
            for (let j = i + 1; j < b.length;j++) {
                right_sum += b[i][j] * X[j]
            }
            new_x[i] = (1 - w) * X[i]  + w * (left_sum + right_sum + c[i])
        }

        let solution_satisfiable = false
        let norma = Math.max(...new_x.map((value, index) => Math.abs(X[index] - new_x[index])));
//        console.log('norma: ', norma)
        if (norma < eps) {
            solution_satisfiable = true;
        }

        X = new_x
        if (solution_satisfiable) {
            break;
        }
    }
    console.log(X)
    console.log(count)
}