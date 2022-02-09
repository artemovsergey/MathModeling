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
}
function gauss(matrix) {
    console.log('===================GAUSS============================')
    print_matrix(matrix)
    const width = matrix[0].length;
    const height = matrix.length;

    for (let h = 0; h < height; h++) {
        const base_row_index = h;

        let maxValue = 0
        let maxIndex = -1
        for (let i = h; i < height; i++) {
            if (Math.abs(matrix[i][h]) > Math.abs(maxValue)) {
                maxIndex = i
                maxValue = matrix[i][h]
            }
        }

        swap_rows(matrix, h, maxIndex)
        print_matrix(matrix)

        for (let i = h; i < height; i++) {
            const normalizer = matrix[i][base_row_index];
            if (isZero(normalizer)) {
                continue;
            }
            for (let j = 0; j < width; j++) {
                if (isNotZero(matrix[i][base_row_index])) {
                    matrix[i][j] /= normalizer
                }
            }
        }
//        console.log('нормализовали')
        print_matrix(matrix)

        for (let i = h + 1; i < height; i++) {
            for (let j = 0; j < width; j++) {
                matrix[i][j] -= matrix[h][j]
            }
        }
//        console.log('отняли')
        print_matrix(matrix)
    }

//    console.log('обратный ход')
    for (let h = height - 1; h >= 0; h--) {
        const base_row_index = h;

        for (let i = h; i >= 0; i--) {
            const normalizer = matrix[i][base_row_index];
            if (isZero(normalizer)) {
                continue;
            }
            for (let j = 0; j < width; j++) {
                if (isNotZero(matrix[i][base_row_index])) {
                    matrix[i][j] /= normalizer
                }
            }
        }

//        console.log('нормализовали')
//        print_matrix(matrix)

        for (let i = h - 1; i >= 0; i--) {
            for (let j = 0; j < width; j++) {
                matrix[i][j] -= matrix[h][j]
            }
        }

//        console.log('отняли')
//        print_matrix(matrix)
    }
    // console.log('нормализируем каждую строку по первому элементу')
    // normilize_by_first_row_element(matrix)
    // print_matrix(matrix)

//    console.log('сортируем строки так чтобы еденицы были на местах с индексами равными индексам строк')
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
            console.log('NO SOLUTION')
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
//            console.log('есть свободная переменная!')
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
                    formula += `-${(-matrix[h][i]).toFixed(2)} * x${i + 1}    `
                }
                console.log(`x${h + 1} = ${formula}`)
            }
        }
    }
}

module.exports = {
    gauss
}