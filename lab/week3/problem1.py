import torch
import torch.nn.functional as F
from random import random 
from typing import Callable

##                         Problem 1                          ##
##                                                            ##
##            Arbitary x_train, y_train are given.            ##
##          In function predict(), you should return          ##
##            list y_test corresponding to x_test.            ##
##               y_train only contains 0 and 1.               ##
##             Therefore, use logstic regression.             ##
##                  Made by @jangyoujin0917                   ##
##                                                            ##

# NOTE : 1. Feel free to use torch.optim and tensor.
#        2. In this problem, we will only grade 'predict' function.
#           Function 'training' is only for modularization.

def training(x_train : list[list[float]], y_train : list[float]) -> tuple[list[float], float]: # DO NOT MODIFY FUNCTION NAME
    pass ### IMPLEMENT FROM HERE


def predict(x_train : list[list[float]], y_train : list[float], x_test : list[list[float]]) -> list[float]: # DO NOT MODIFY FUNCTION NAME
    w, b = training(x_train, y_train)
    ### IMPLEMENT FROM HERE

if __name__ == "__main__":
    # This is very simple case. Passing this testcase do not mean that the code is perfect.
    # Please consider for the practial problems when score is not high.
    x_train = [[0., 1.], [1., 0.], [2., 5.], [3., 1.], [4., 2.]]
    y_train = [0., 0., 1., 0., 1.]
    x_test = [[7., 2.], [1.5, 1.], [2.5, 0.5]]
    
    y_test = predict(x_train, y_train, x_test)

    print(y_test)