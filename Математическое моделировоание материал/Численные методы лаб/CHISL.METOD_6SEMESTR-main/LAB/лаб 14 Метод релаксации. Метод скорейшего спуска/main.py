import data as dat
import config

from slae import *

print("Relaxation method:\n")
method_relaxation(dat.MATRIX, dat.W, dat.E, config.NAME_MATRIX, config.NAME_UNKNOWN)

print("Rapid descent method:\n")
method_rapid_descent(dat.MATRIX1, dat.E1, config.NAME_MATRIX, config.NAME_UNKNOWN)
