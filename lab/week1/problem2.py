from jax import grad
from random import random 
from typing import Callable


##                        Problem 2                           ##
##                                                            ##
##           Arbitrary quartic function will be given.        ##
## Return the optimal point(global minimum) of given function ##
##                                                            ##
##                  Made by @jangyoujin0917                   ##
##                                                            ##


def test_func(x): # function for testing; function for evaluation will be different.
    return x ** 4


def solution(func: Callable, start_point: float): # DO NOT MODIFY FUNCTION NAME
    ### IMPLEMENT FROM HERE
    

if __name__ == '__main__':
    print(solution(test_func, 10*random()))
