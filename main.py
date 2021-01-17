from math import *

def derivation(x,func):
    e = 0.0001
    pr = (func(x + h) - func(x)) / h
    return round(pr,2)
