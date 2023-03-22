import torch
from random import random 
from typing import Callable

##                         Problem 2                          ##
##                                                            ##
##            Arbitary x_train, y_train are given.            ##
##     In this problem, x_train is list of list of float.     ##
##   Suppose that x and y have linear correlation, y=wx+b.    ##
##           (In this problem, w will be a vector.)           ##
##     In function training(), you should return [w, b].      ##
##          In function predict(), you should return          ##
##            list y_test corresponding to x_test.            ##
##                  Made by @jangyoujin0917                   ##
##                                                            ##

# NOTE : Feel free to use torch.optim and tensor.

def training(x_train : list[list[float]], y_train : list[float]) -> tuple[list[float], float]: # DO NOT MODIFY FUNCTION NAME
    # data normalization
    # 1. Prevents overflow when calculating MSE
    # 2. Prevents underfitting
    # Note that you need to convert [w, b] to the original scale.
    # w = w * (y_max - y_min)
    # b = b * (y_max - y_min) + y_min
    y_min = min(y_train)
    y_max = max(y_train)
    normalize = lambda y : (y - y_min)/(y_max - y_min)
    
    ### IMPLEMENT FROM HERE


def predict(x_train : list[list[float]], y_train : list[float], x_test : list[list[float]]) -> list[float]: # DO NOT MODIFY FUNCTION NAME
    pass ### IMPLEMENT FROM HERE

if __name__ == "__main__":
    x_train = [[0., 1.], [1., 0.], [2., 2.], [3., 1.], [4., 3.]]
    y_train = [3., 2., 7., 6., 11.] # y = x_0 + 2*x_1 + 1 # Note that not all test cases give clear line.
    x_test = [[5., 3.], [10., 6.], [8., 9.]]
    
    w, b = training(x_train, y_train)
    y_test = predict(x_train, y_train, x_test)

    print(w, b)
    print(y_test)