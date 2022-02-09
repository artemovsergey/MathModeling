const {
  generate_vector,
  clone,
  generate_matrix,
  generate_square_matrix,
  extract_last_column_from,
  mulitply_matrices,
  to_vector,
  subtract_vectors,
  extract_square_matrix_from,
  transpose,
  multiply_matrix_on_scalar,
  print_matrix,
} = require("./utils");

 const matrix = [
     [6.25, -1, 0.5, 7.5],
     [-1, 5, 2.12, -8.68],
     [0.5, 2.12, 3.6, -0.24]
 ]
relax_with(matrix);

function relax_with(matrix) {
  const square_matrix = extract_square_matrix_from(matrix);
  let x = generate_vector(matrix.length);

  const eps = 0.001
  let iterations = 0;
    while (true) {
      iterations++;
        // console.log(to_vector(mulitply_matrices(square_matrix, x)))
        // console.log(extract_last_column_from(matrix))
        const r0 = subtract_vectors(
        to_vector(mulitply_matrices(square_matrix, x)),extract_last_column_from(matrix));
        const ATr0 = mulitply_matrices(transpose(square_matrix), r0)
        const AAr0 = to_vector(mulitply_matrices(square_matrix,ATr0));
      
        let numerator = 0;
        for (let i = 0; i < AAr0.length; i++) {
          numerator += AAr0[i] * r0[i];
        }
        let denominator = 0;
        for (let i = 0; i < AAr0.length; i++) {
          denominator += AAr0[i] ** 2;
        }
        const uu = numerator / denominator;
      
        const x1 = subtract_vectors(
        x,multiply_matrix_on_scalar(mulitply_matrices(transpose(square_matrix), r0), uu));
        let norma = Math.max(...x1.map((value, index) => Math.abs(x[index] - x1[index])));
        
//        console.log('norma: ', norma)
        let solution_satisfiable = false;
        if (norma < eps) {
            solution_satisfiable = true;
        }
        x = x1;

        if (solution_satisfiable) {
          break;
        }
    }
    console.log(x)
    console.log(iterations)
}