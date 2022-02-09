const { find_determinant } = require("./src/find_determinant");
const { find_reverse_matrix_using_jordan } = require("./src/find_reverse_matrix_using_jordan");
const { find_reverse_matrix } = require("./src/find_reverse_matrix_using_lu");
const { jordan_gauss } = require("./src/jordan_gauss");
const { read_matrix } = require("./src/read_matrix");

//find_determinant(read_matrix());
find_reverse_matrix(read_matrix())
//find_reverse_matrix_using_jordan(read_matrix())