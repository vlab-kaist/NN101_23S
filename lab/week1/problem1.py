import torch
from random import random 
from typing import Callable


##                        Problem 1                           ##
##                                                            ##
##         Arbitrary quadratic function will be given.        ##
## Return the optimal point(global minimum) of given function ##
##          Condition: highest order term is positive         ##
##                  Made by @jangyoujin0917                   ##
##                                                            ##


def solution(func: Callable, start_point: float): # DO NOT MODIFY FUNCTION NAME    
    pass ### IMPLEMENT FROM HERE
    

if __name__ == '__main__':
    def test_func(x): # function for testing;function for evaluation will be different.
        return x ** 2
    t = torch.tensor([10*random()], requires_grad=True, dtype=torch.float32)
    print(solution(test_func, t))