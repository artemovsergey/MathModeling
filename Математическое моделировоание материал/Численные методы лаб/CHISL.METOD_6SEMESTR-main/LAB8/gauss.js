const { print_matrix, clone, swap_rows } = require("./utils");

function isZero(value) {
    return Math.abs(value) <= 0.00001
}
function isNotZero(value) {
    return !isZero(value)
}

function normilize_by_first_row_element(matrix) {
    for (let h = 0;h < matrix.length; h++) {
        let not_zero_element = undefined;
        for (let w = 0; w < matrix[0].length; w++) {
            if (isNotZero(matrix[h][w]) && not_zero_element === undefined) {
                not_zero_element = matrix[h][w]
                break;
            }
        }

        if (not_zero_element !== undefined) {
            for (let w = 0; w < matrix[0].length; w++) {
                matrix[h][w] /= not_zero_element;
            }
        }
    }
    print_matrix(matrix)
}

function sort_rows_by_one_position(matrix) {
    let placed_rows = []
    for (let i = 0; i < matrix.length; i++) {
        for (let h = 0; h < matrix.length; h++) {
            if (placed_rows.includes(h)) {
                continue;
            }
            if (matrix[h][i] === 1) {
                swap_rows(matrix, i, h)
                placed_rows.push(i)
            }
        }
    }
    print_matrix(matrix)
}

function gauss(matrix) {
    console.log('===================GAUSS============================')
    const width = matrix[0].length;
    const height = matrix.length;
    print_matrix(matrix)

    for (let h = 0; h < height; h++) {
        const base_row_index = h;

        for (let target_row_index = base_row_index + 1; target_row_index < height; target_row_index++) {
            // let first_not_zero_index = 0;
            // for (let i = 0; i < width; i++) {
            //     if (isNotZero(matrix[target_row_index][i])) {
            //         first_not_zero_index = i
            //         break;
            //     }
            // }

            if (isZero(matrix[base_row_index][base_row_index])) {
                continue;
            }
            const multiplier = matrix[target_row_index][base_row_index] / matrix[base_row_index][base_row_index] 
//            console.log(`отнимаем от строки №${(target_row_index + 1).toFixed(0)} строку №${(base_row_index + 1).toFixed(0)} умноженную на ${multiplier}`)
            for (let i = 0; i < width; i++) {
                matrix[target_row_index][i] -= matrix[base_row_index][i] * multiplier
            }
        }
        print_matrix(matrix)
        const matrix_copy = clone(matrix)
        for (let i = 0; i < width; i++) {
            const normalizer = matrix_copy[base_row_index][base_row_index];
            if (isNotZero(matrix[base_row_index][base_row_index])) {
                matrix[base_row_index][i] /= normalizer
            }
        }
        print_matrix(matrix)
    }

    console.log('REVERSE STEP')
    for (let h = height -1; h >= 0; h--) {
        const base_row_index = h;

        for (let target_row_index = base_row_index - 1; target_row_index >= 0; target_row_index--) {
            // let first_not_zero_index = 0;
            // for (let i = 0; i < width; i++) {
            //     if (isNotZero(matrix[target_row_index][i])) {
            //         first_not_zero_index = i
            //         break;
            //     }
            // }

            if (isZero(matrix[base_row_index][base_row_index])) {
                continue;
            }
            const multiplier = matrix[target_row_index][base_row_index] / matrix[base_row_index][base_row_index]
//            console.log(`отнимаем от строки №${(target_row_index + 1).toFixed(0)} строку №${(base_row_index + 1).toFixed(0)} умноженную на ${multiplier}`)
            for (let i = width - 1; i >=0; i--) {
                matrix[target_row_index][i] -= matrix[base_row_index][i] * multiplier
            }
        }

        for (let i = 0; i < width; i++) {
            if (isNotZero(matrix[base_row_index][base_row_index])) {
                matrix[base_row_index][i] /= matrix[base_row_index][base_row_index]
            }
        }
        print_matrix(matrix)
    }

    console.log('NORMALIZE EACH ROW BY THE FIRST ELEMENT')
    normilize_by_first_row_element(matrix)
    print_matrix(matrix)

    console.log('SORTING THE ROWS')
    sort_rows_by_one_position(matrix)
    print_matrix(matrix)

    for (let h = 0; h < height; h++) {
        let all_zeros = true;
        for (let i = 0; i < matrix[h].length - 1; i++) {
            if (isNotZero(matrix[h][i])) {
                all_zeros = false;
                break;
            }
        }
        if (all_zeros && isNotZero(matrix[h][matrix[h].length - 1])) {
            console.log('NO SOLUTIONS')
            return;
        }
    }

    let has_free_variale = false;
    for (let h = 0; h < height; h++) {
        let all_zeros = true;
        for (let i = 0; i < matrix[h].length; i++) {
            if (isNotZero(matrix[h][i])) {
                all_zeros = false;
                break;
            }
        }

        if (all_zeros) {
            console.log('A FREE VARIABLE WAS FOUND')
            has_free_variale = true;
            break;
        }
    }

    if (!has_free_variale) {
        for (let i = 0;i < height; i++) {
            console.log(matrix[i][matrix[i].length - 1])
        }
    } else {
        for (let h = 0; h < height; h++) {
            let all_zeros = true;
            for (let i = 0; i < matrix[h].length; i++) {
                if (isNotZero(matrix[h][i])) {
                    all_zeros = false;
                    break;
                }
            }
            if (all_zeros) {
                console.log(`x${h + 1} = free`)
            } else {
                let formula = `${matrix[h][matrix[0].length - 1]} `

                for (let i = h + 1; i < width - 1; i++) {
                    formula += `-${(matrix[h][i]).toFixed(2)} * x${i + 1}    `
                }
                console.log(`x${h + 1} = ${formula}`)
            }
        }
    }
}

module.exports = {
    gauss
}