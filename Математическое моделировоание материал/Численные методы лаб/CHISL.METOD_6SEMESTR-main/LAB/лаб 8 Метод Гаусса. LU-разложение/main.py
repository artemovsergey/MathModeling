import data as dat
import config
import copy

from slae import *


print("Method Gauss:\n")
method_gauss(copy.deepcopy(dat.MATRIX), config.ACCURACY_PRINT, config.NAME_MATRIX, config.NAME_UNKNOWN)

print("Method LU decomposition:\n")
method_lu_decomposition(dat.MATRIX, config.ACCURACY_PRINT, config.NAME_MATRIX)
