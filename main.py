from math import *

def derivation(x,func):
    e = 0.0001
    pr = (func(x + e) - func(x)) / e
    return round(pr,2)
