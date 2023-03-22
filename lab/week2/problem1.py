import torch
from random import random 
from typing import Callable

##                         Problem 1                          ##
##                                                            ##
##            Arbitary x_train, y_train are given.            ##
##   Suppose that x and y have linear correlation, y=wx+b.    ##
##     In function training(), you should return [w, b].      ##
##          In function predict(), you should return          ##
##            list y_test corresponding to x_test.            ##
##                  Made by @jangyoujin0917                   ##
##                                                            ##

# NOTE : Feel free to use torch.optim and tensor.

def training(x_train : list[float], y_train : list[float]) -> list[float]: # DO NOT MODIFY FUNCTION NAME
    # Data normalization code (prevents overflow when calculating MSE, prevents underfitting)
    # Note that you need to convert [w, b] to the original scale before returning value
    # w = w * (y_max - y_min)
    # b = b * (y_max - y_min) + y_min
    y_min = min(y_train)
    y_max = max(y_train)
    normalize = lambda y : (y - y_min)/(y_max - y_min)

    ### IMPLEMENT FROM HERE


def predict(x_train : list[float], y_train : list[float], x_test : list[float]) -> list[float]: # DO NOT MODIFY FUNCTION NAME
    pass ### IMPLEMENT FROM HERE

if __name__ == "__main__":
    x_train = [0.0, 1.0, 2.0, 3.0, 4.0]
    y_train = [2.0, 4.0, 6.0, 8.0, 10.0] # Note that not all test cases give clear line.
    x_test = [5.0, 10.0, 8.0]
    
    w, b = training(x_train, y_train)
    y_test = predict(x_train, y_train, x_test)

    print(w, b)
    print(y_test)
