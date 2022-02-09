const { generate_square_matrix, print_matrix, extract_last_column_from, generate_vector, on_every_row, reduce_to_vector, transpose, map_matrix } = require("./utils");

function resolve(matrix) {
//    matrix = map_matrix(matrix, (e) => Math.abs(e))
//    console.log(matrix)
    const height = matrix.length;
    const width = matrix[0].length - 1;
    const width_with_solution = width + 1
    const last_column = extract_last_column_from(matrix)
    const result = generate_square_matrix(height)
    
    //для первой строки
    for (let i = 0; i < width; i++) {
        if (i === 0) {
            result[0][0] = Math.sqrt(matrix[0][i])
        } else {
            result[0][i] = matrix[0][i] / result[0][0]
        }
        console.log(`element ${0 + 1}:${i + 1} = ${result[0][i]}`)
    }
    
    //для остальных
    for (let i = 1; i < height; i++) {
        // для Uii элемента
        let sum = 0;
        for (let k = 0; k < i; k++) {
            sum += result[k][i] ** 2
        }
        result[i][i] = Math.sqrt(matrix[i][i] - sum)
        console.log(`element ${i + 1}:${i + 1} = ${result[i][i]}`)

        for (let j = i + 1; j < width; j++) {
            let sum = 0;
            for (let k = 0; k < i; k++) {
                sum += result[k][i] * result[k][j]
            }

            result[i][j] = (1 / result[i][i]) * (matrix[i][j] - sum)
            console.log(`element ${i + 1}:${j + 1} = ${result[i][j]}`)
        }
    }
    print_matrix(result)

    const y_vector = generate_vector(height);
    const transposed_matrix = transpose(result)
    console.log(transposed_matrix)

    for (let i = 0;i < height; i++) {
        let r = last_column[i]
        for (let j = 0; j < width; j++) {
            if (j === i) {
                continue;
            }
            r -= transposed_matrix[i][j] * y_vector[j];
        }
        if (r !== 0) {
            y_vector[i] = r / transposed_matrix[i][i];
        } else {
            y_vector[i] = 0
        }
    }

    console.log('y vector', y_vector)

    const result_vector = generate_vector(height)

    for (let i = height - 1;i >= 0; i--) {
        let r = y_vector[i]
        for (let j = 0; j < width; j++) {
            if (j === i) {
                continue;
            }
            r -= result[i][j] * result_vector[j];
        }
        if (r !== 0) {
            result_vector[i] = r / result[i][i];
        } else {
            result_vector[i] = 0
        }
    }
    console.log(result_vector)
}

module.exports = {
    resolve
}