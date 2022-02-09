const { gauss } = require("./gauss")
const { jordan_gauss } = require("./jordan_gauss")
const { read_matrix } = require("./read_matrix")

gauss(read_matrix())
//console.log("====================================")
//jordan_gauss(read_matrix())