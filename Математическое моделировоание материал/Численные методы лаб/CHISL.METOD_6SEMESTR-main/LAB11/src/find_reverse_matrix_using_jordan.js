const { generate_identity_matrix, extend_matrix, print_matrix, extract_last_n_columns } = require("./utils");
const { jordan_gauss } = require('./jordan_gauss')

function find_reverse_matrix_using_jordan(matrix) {
    const identity = generate_identity_matrix(matrix.length)

    const matrix_task = extend_matrix(matrix, identity);
    const result = jordan_gauss(matrix_task)
    console.log('after the transformations')
    print_matrix(result)

    const inverse_matrix = extract_last_n_columns(result, matrix.length)
    console.log('=====================================')
    print_matrix(inverse_matrix)
}

module.exports = {
    find_reverse_matrix_using_jordan
}