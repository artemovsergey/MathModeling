import data as dat
import config
import copy

from slae import *

print("Method gauss with the selection of the main element:\n")
method_gauss_select_main_element(copy.deepcopy(dat.MATRIX), config.ACCURACY_PRINT, config.NAME_MATRIX,
                                 config.NAME_UNKNOWN)

print("Method Jordan-Gauss:\n")
method_jordan_gauss(dat.MATRIX, config.ACCURACY_PRINT, config.NAME_MATRIX, config.NAME_UNKNOWN)
