module.exports = {
    clone, 
    swap_rows,
    print_matrix,
    generate_vector,
    generate_square_matrix,
    extract_square_matrix_from,
    extract_last_column_from,
    on_every_row,
    reduce_to_vector,
    transpose,
    extend_matrix,
    generate_identity_matrix,
    extract_column,
    reverse,
    extract_last_n_columns,
    generate_matrix,
    mulitply_matrices: multiplyMatrices,
    to_vector,
    subtract_vectors,
    multiply_matrix_on_scalar,
}

function subtract_vectors(vector1, vector2) {
    const result_vector = generate_vector(vector1.length)

    for (let i = 0;i < vector1.length; i++) {
        result_vector[i] = vector1[i] - vector2[i]
    }
    return result_vector
}

function multiply_matrix_on_scalar(matrix, scalar) {
    const result = clone(matrix)
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0;j < matrix[i].length; j++) {
            result[i][j] *= scalar
        }
    }
    return result;
}
function multiplyMatrices (a, b) {

    if (!Array.isArray(b[0])) {
        b = b.map(e => [e])
    }
    if (!Array.isArray(a[0])) {
        a = a.map(e => [e])
    }
    if (!Array.isArray(a) || !Array.isArray(b) || !a.length || !b.length) {
       throw new Error('arguments should be in 2-dimensional array format');
    }
    let x = a.length,
    z = a[0].length,
    y = b[0].length;
    if (b.length !== z) {
       // XxZ & ZxY => XxY
        throw new Error("INVALID MATRICES")
    }
    let productRow = Array.apply(null, new Array(y)).map(Number.prototype.valueOf, 0);
    let product = new Array(x);
    for (let p = 0; p < x; p++) {
       product[p] = productRow.slice();
    }
    for (let i = 0; i < x; i++) {
       for (let j = 0; j < y; j++) {
          for (let k = 0; k < z; k++) {
             product[i][j] += a[i][k] * b[k][j];
          }
       }
    }
    return product;
 }

 function to_vector(vector_matrix) {
     return vector_matrix.map(vm => vm[0])
 }
function iterate_matrix(matrix, callback) {
    for (let i = 0;i < matrix.length; i++) {
        for (let j = 0; j < matrix[0].length; j++) {
            callback(matrix[i][j], i, j)
        }
    }
}
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

function generate_matrix(height, width) {
    let matrix = []
    for (let i = 0; i < height; i++) {
        matrix.push(generate_vector(width));
    }
    return matrix;
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
function extract_last_n_columns(matrix, start_from) {
    const height = matrix.length;
    const width = matrix[0].length;
    const result = generate_matrix(matrix.length, matrix[0].length - start_from);
    for (let i = 0; i < height; i++) {
        for (let j = start_from; j < width; j++) {
            result[i][j - start_from] = matrix[i][j]
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

function on_every_row(matrix, callback) {
    for (let i = 0;i < matrix.length; i++) {
        callback(matrix[i], i)
    }
}

function reduce_to_vector(matrix, reducer) {
    const vector = generate_vector(matrix.length);

    on_every_row(matrix, (row, i) => {
        let result = 0;
        row.forEach((e, j) => {
            reducer(result, e, i, j)
        })
        vector[i] = result;
    })
    return vector;
}

function extend_matrix(matrix, vector_column) {
    matrix = clone(matrix);
    for (let i = 0; i < matrix.length; i++) {
        if (vector_column[i][0] !== undefined) {
            vector_column[i].forEach(e => {
                matrix[i].push(e)
            })
        } else {
            matrix[i].push(vector_column[i])
        }
    }
    return matrix
}
function transpose(matrix) {
    return matrix[0].map((col, i) => matrix.map(row => row[i]));
}

function generate_identity_matrix (size) {
    const matrix = generate_square_matrix(size);
    for (let i = 0;i< matrix.length; i++) {
        matrix[i][i] = 1;
    }
    return matrix
}
function extract_column(matrix, column_index) {
    const vector = generate_vector(matrix.length);
    for (let i = 0; i < matrix.length; i++) {
        vector[i] = matrix[i][column_index]
    }
    return vector;
}

function reverse(vector) {
    return clone(vector).reverse();
}





