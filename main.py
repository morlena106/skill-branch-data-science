from math import *

def derivation(x,func):
    e = 0.0001
    pr = (func(x + e) - func(x)) / e
    return round(pr,2)

def gradient(xlist, func):
    e = 0.0001
    x1 = xlist[0]
    x2 = xlist[1]
    pr1 = (func(x1 + e, x2) - func(x1, x2)) / e
    pr2 = (func(x1, x2 + e) - func(x1, x2)) / e
    grad = [round(pr1,2),round(pr2,2)]
    return grad
