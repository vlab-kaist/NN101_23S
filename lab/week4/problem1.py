import torch
import torch.nn.functional as F
import numpy as np

##                         Problem 1                          ##
##                                                            ##
##           Given Iris_train.csv, train your model           ##
##              to predict the species of iris.               ##
##            In the implementation of functions,             ##
##                  opening file is invalid.                  ##
## Checker will provide Iris_train.csv with x_train, y_train. ##
## LIMITS : Do not reference dataset on Internet in the code. ##
##        (Since test datas are also on the Internet.)        ##
##                  Made by @jangyoujin0917                   ##
##                                                            ##

# NOTE : Data normalization may help you to get good score.

iris = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]
def iris_onehot(x : str) -> list[int]:
    index = iris.index(x)
    return list(np.eye(len(iris))[index])

def training(x_train : torch.Tensor, y_train : torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]: # DO NOT MODIFY FUNCTION NAME
    pass ### IMPLEMENT FROM HERE

def predict(x_train : torch.Tensor, y_train : torch.Tensor, x_test : torch.Tensor) -> torch.Tensor: # DO NOT MODIFY FUNCTION NAME
    # predict() should return the index of the answer.
    # Therefore, the return value is 1d-tensor that only contains 0, 1, 2. 
    w, b = training(x_train, y_train)
    ### IMPLEMENT FROM HERE

if __name__ == "__main__":
    import csv
    with open("Iris_train.csv", "r") as f: # Make sure that Iris_train.csv is in same directory.
        rdr = csv.reader(f)
        contents = [i for i in rdr]
    contents = contents[1:]
    x = torch.tensor([[float(j) for j in i[:-1]] for i in contents], dtype=torch.float32)
    y = torch.tensor([iris_onehot(i[-1]) for i in contents], dtype=torch.float32)
    test = torch.tensor([[5.1,3.0,1.2,0.3], [5.1,3.4,4.1,1.3]], dtype=torch.float32)

    prediction = predict(x, y, test)
    print(prediction)