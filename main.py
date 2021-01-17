from math import *

def derivation(x,func):
    e = 0.0001
    pr = (func(x + e) - func(x)) / e
    return round(pr,2)

def gradient(xlist, func):
    e = 0.00001
    x1 = xlist[0]
    x2 = xlist[1]
    pr1 = (func([x1 + e, x2]) - func([x1, x2])) / e
    pr2 = (func([x1, x2 + e]) - func([x1, x2])) / e
    grad = [round(pr1,2),round(pr2,2)]
    return grad
    
def gradient_optimization_one_dim(func):
    e = 0.001
    x = 10
    for i in range(50):
        pr = (func(x + e) - func(x)) / e
        x = x - e*pr
    return round(x, 2)

def gradient_optimization_multi_dim(func):
    e = 0.001
    x1 = 4
    x2 = 10
    
    for i in range(50):

        x = [x1, x2]
        x_1 = [x1 + e, x2]
        x_2 = [x1, x2 + e]

        pr1 = (func(x_1) - func(x)) / e
        pr2 = (func(x_2) - func(x)) / e

        x1 = x1 - e * pr1
        x2 = x2 - e * pr2

        x1 = round(x1, 2)
        x2 = round(x2, 2)
        
    x = [x1, x2]
    return x
