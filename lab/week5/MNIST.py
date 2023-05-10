import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
import torchvision.transforms as T
import numpy as np

##                         Problem 1                          ##
##                                                            ##
##          Given MNIST train data, train your model.         ##
## LIMITS : Do not reference dataset on Internet in the code. ##
##        (Since test datas are also on the Internet.)        ##
##                  Made by @jangyoujin0917                   ##
##                                                            ##

# NOTE : 1. Data is already normalized.
#        2. This problem is not for submit.
def one_hot(x: int) -> torch.Tensor:
    return torch.tensor(np.eye(10)[x])

learning_rate = 1e-2 # You can adjust this.
class Model(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.seq = nn.Sequential(
            ## MAKE YOUR OWN NeuralNet MODELS!
            ## INPUT : [BATCH_SIZE, 784]
            ## OUTPUT : [BATCH_SIZE, 10]
        )
    
    def forward(self, x):
        return self.seq(x)

def training(train_loader: torch.utils.data.DataLoader) -> nn.Module: # DO NOT MODIFY FUNCTION NAME
    model = Model()
    optimizer = torch.optim.Adam(model.parameters(), lr = learning_rate, betas=(0.9, 0.999))
    epoch_num = 10

    for epoch in range(epoch_num):
        for data, target in train_loader:
            optimizer.zero_grad()
            output = model(data)
            loss = nn.CrossEntropyLoss()(output, target)
            loss.backward()
            optimizer.step()
        print("Epoch : {} \t Loss : {:3f}".format(epoch+1, loss.item()))
    
    return model

def predict(train_loader: torch.utils.data.DataLoader, x_test : torch.Tensor) -> torch.Tensor: # DO NOT MODIFY FUNCTION NAME
    model = training(train_loader)
    with torch.no_grad():
        hypothesis = torch.argmax(model(x_test).squeeze(), dim=1)
    return hypothesis

if __name__ == "__main__":
    train_data = torchvision.datasets.MNIST('./data', train=True, download=True, transform=T.Compose([T.ToTensor(), T.Lambda(lambda x: torch.flatten(x))]))
    test_data = torchvision.datasets.MNIST('./data', train=False, download=True, transform=T.Compose([T.ToTensor(), T.Lambda(lambda x: torch.flatten(x))]))
    train_loader = torch.utils.data.DataLoader(dataset=train_data, batch_size=64, shuffle=True)
    test_loader = torch.utils.data.DataLoader(dataset=test_data, shuffle=False)
    
    x_test = torch.stack([i[1][0] for i in enumerate(test_loader)], 0)
    y_test = torch.tensor([i[1][1] for i in enumerate(test_loader)])
    result = predict(train_loader, x_test)
    score = (result == y_test).sum() / len(y_test) * 100
    print(score)