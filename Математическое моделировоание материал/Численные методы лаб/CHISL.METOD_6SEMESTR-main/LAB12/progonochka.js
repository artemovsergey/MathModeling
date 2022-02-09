const { generate_vector, extract_last_column_from } = require("./utils")

function read_matrix() {
    return [
      [2, 1, 0, 0, 4],
      [2, 3, -1, 0, 9],
      [0, 1, -1, 3, 12],
      [0, 0, 1, -1, -4]
    ]
//    return [
//      [3.36, 0.92, 0, 2.15],
//      [0.92, 2.24, 0.77, -2.06],
//      [0.77, -3.16, 0.97]
//    ]
//    return [
//      [5.63, -1.72, 0, -0.75],
//      [-1.72, -3.27, 0.62, 1.27],
//      [0, 0.62, -4.43, 2.74]
//    ]
}
progonochka(read_matrix())

function progonochka(matrix) {
    const f = extract_last_column_from(matrix)
    const a_diagonal = []

    for (let i = 0; i < matrix.length - 1; i++) {
        a_diagonal.push(matrix[i + 1][i])
    }
//    console.log('diagonal a: ', a_diagonal)
    a_diagonal.unshift(undefined)//первый элемент у нижней диагонали не существует

    const b_diagonal = []
    for (let i = 0; i < matrix.length; i++) {
        b_diagonal.push(matrix[i][i])
    }
//    console.log('diagonal b: ', b_diagonal)

    const c_diagonal = []
    for (let i = 0; i < matrix.length - 1; i++) {
        c_diagonal.push(matrix[i][i + 1])
    }
//    console.log('diagonal c: ', c_diagonal)

    const A = generate_vector(matrix.length - 1)
    const B = generate_vector(matrix.length - 1)
//    console.log('straight run')

    //для первых элементов
    A[0] = - c_diagonal[0] / b_diagonal[0]
    B[0] = f[0] / b_diagonal[0]

    console.log(`A1 = ${A[0]}`)
    console.log(`B1 = ${B[0]}`)

    //для остальных
    for (let i = 1; i < matrix.length - 1; i++) {
        A[i] = - c_diagonal[i] / (A[i - 1] * a_diagonal[i] + b_diagonal[i])
        B[i] = ( f[i] - a_diagonal[i] * B[i - 1]) / (A[i - 1] * a_diagonal[i] + b_diagonal[i])

        console.log(`A${i + 1} = ${A[i]}`)
        console.log(`B${i + 1} = ${B[i]}`)
    }

    //обратный ход
    //для последнего
    const last_index = matrix.length - 1;
    const x_last = (f[last_index] - a_diagonal[last_index] * B[last_index - 1]) / (b_diagonal[last_index] + a_diagonal[last_index] * A[last_index - 1])
    console.log(`x${last_index + 1} = ${x_last}`)

    //для остальных
    let previous_x = x_last;
    for (let i = last_index - 1; i >= 0; i--) {
        const x = A[i] * previous_x + B[i] 
        console.log(`x${i + 1} = ${x}`)
        previous_x = x
    }
}

module.exports = {
    progonochka
}