import data as dat
import config

from matrix import *

print("LU decomposition:\n")
print("det({0}) = {1!s}\n".format(config.NAME_MATRIX, round(getDet_LU_decomposition(dat.MATRIX, config.NAME_MATRIX,
                                                                    config.ACCURACY_PRINT),  config.ACCURACY_PRINT)))
print("Inverse matrix(LU-decomposition):\n")
getInverseMatrix_LU_decomposition(dat.MATRIX, config.NAME_MATRIX, config.ACCURACY_PRINT)

print("Inverse matrix(Jordan-Gauss method):\n")
getInverseMatrix_JordanGauss(dat.MATRIX, config.NAME_MATRIX, config.ACCURACY_PRINT)
