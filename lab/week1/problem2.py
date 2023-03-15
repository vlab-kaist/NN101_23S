import torch
from random import random 
from typing import Callable


##                        Problem 2                           ##
##                                                            ##
##           Arbitrary quartic function will be given.        ##
## Return the optimal point(global minimum) of given function ##
##          Condition: highest order term is positive         ##
##                  Made by @jangyoujin0917                   ##
##                                                            ##


def solution(func: Callable, start_point: float) -> float: # DO NOT MODIFY FUNCTION NAME    
    pass ### IMPLEMENT FROM HERE
    

if __name__ == '__main__':
    def test_func(x): # function for testing;function for evaluation will be different.
        return x ** 4
    t = 10*random()
    print(solution(test_func, t))