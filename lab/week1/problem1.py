from jax import grad
from random import random 
from typing import Callable


##                        Problem 1                           ##
##                                                            ##
##         Arbitrary quadratic function will be given.        ##
## Return the optimal point(global minimum) of given function ##
##          Condition: highest order term is positive         ##
##                  Made by @jangyoujin0917                   ##
##                                                            ##


def test_func(x): # function for testing;function for evaluation will be different.
    return x ** 2


def solution(func: Callable, start_point: float): # DO NOT MODIFY FUNCTION NAME    
    ### IMPLEMENT FROM HERE
    

if __name__ == '__main__':
    print(solution(test_func, 10*random()))
