const { gauss } = require("./gauss")
const { read_matrix } = require("./read_matrix")
const { use_lu } = require("./use_lu")

gauss(read_matrix())
// use_lu(read_matrix())