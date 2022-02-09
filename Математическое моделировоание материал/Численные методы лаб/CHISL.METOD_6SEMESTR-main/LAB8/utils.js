function clone(anything) {
    return JSON.parse(JSON.stringify(anything))
}

function swap_rows(matrix, first, second) {
    if (first === second) {
        return;
    }
    const temp_row = clone(matrix[first])
    matrix[first] = clone(matrix[second])
    matrix[second] = temp_row;
}

function print_matrix(matrix) {
    for (let i = 0; i < matrix.length; i++) {
        let row = ""
        for (let j = 0; j < matrix[i].length; j++) {
            row += ` ${matrix[i][j].toFixed(2)} `
        }
        console.log(row)
    }
    console.log("======================================")

}


function generate_vector(size) {
    let vector = []
    for (let i = 0; i < size; i++) {
        vector.push(0)
    }
    return vector;
}

function generate_square_matrix(size) {
    let matrix = []
    for (let i = 0; i < size; i++) {
        matrix.push(generate_vector(size));
    }
    return matrix;
}

function extract_square_matrix_from(matrix) {
    const height = matrix.length;
    const result = generate_square_matrix(matrix.length);
    for (let i = 0; i < height; i++) {
        for (let j = 0; j < height; j++) {
            result[i][j] = matrix[i][j]
        }
    }
    return result;
}
function extract_last_column_from(matrix) {
    const height = matrix.length;
    const width = matrix[0].length;
    const result = generate_vector(matrix.length);
    for (let i = 0; i < height; i++) {
        result[i] = matrix[i][width - 1]
    }
    return result;
}

function simple_print_matrix() {
    return;
    for (let i = 0; i < matrix.length; i++) {
        let row = ""
        for (let j = 0; j < matrix[i].length; j++) {
            row += ` ${matrix[i][j].toFixed(2)} `
        }
        console.log(row)
    }
    console.log("======================================")
}
module.exports = {
    clone, 
    swap_rows,
    print_matrix,
    generate_vector,
    generate_square_matrix,
    extract_square_matrix_from,
    extract_last_column_from,
    simple_print_matrix,
}