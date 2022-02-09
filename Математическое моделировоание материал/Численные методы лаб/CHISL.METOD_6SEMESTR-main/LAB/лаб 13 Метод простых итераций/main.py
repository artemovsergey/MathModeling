import data as dat
import copy
import config

from slae import *

print("Method Jacobi:\n")
method_jacobi(copy.deepcopy(dat.MATRIX), dat.E1, config.NAME_MATRIX, config.NAME_UNKNOWN)

print("Method Seidel:\n")
method_seidel(dat.MATRIX, dat.E2, config.NAME_MATRIX, config.NAME_UNKNOWN)
