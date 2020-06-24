import sys
sys.path.insert(0, '..')
import d2l
from d2l.data import load_data_fashion_mnist
from d2l.train import train_ch3

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

class Net(nn.Module):
    def __init__(self, num_inputs = 784, num_outputs = 10, num_hiddens = 256, is_training = True):
        super(Net, self).__init__()
        
        self.num_inputs = num_inputs
        self.num_outputs = num_outputs
        self.num_hiddens = num_hiddens
        
        self.linear_1 = nn.Linear(num_inputs, num_hiddens)
        self.linear_2 = nn.Linear(num_hiddens, num_outputs)
        
        self.relu = nn.ReLU()
    def forward(self, X):
        X = X.reshape((-1, self.num_inputs))
        H1 = self.relu(self.linear_1(X))
        out = self.linear_2(H1)
        return out   
    
net = Net()
print(net)

num_epochs, lr, batch_size = 10, 0.5, 256
train_iter, test_iter = load_data_fashion_mnist(batch_size)
criterion = nn.CrossEntropyLoss()
train_ch3(net, train_iter, test_iter, criterion, num_epochs, batch_size, lr)

