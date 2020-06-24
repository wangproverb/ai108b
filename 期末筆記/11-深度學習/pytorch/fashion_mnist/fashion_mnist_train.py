import sys
sys.path.insert(0, '..')
import d2l
import torch
import torch.nn as nn

batch_size = 256
train_iter, test_iter = d2l.load_data_fashion_mnist(batch_size)

class Reshape(torch.nn.Module):
    def forward(self, x):
        return x.view(-1,784)
    
net = nn.Sequential(Reshape(), nn.Linear(784, 10))

def init_weights(m):
    if type(m) == nn.Linear:
        torch.nn.init.normal_(m.weight, std=0.01)

net.apply(init_weights)

loss = nn.CrossEntropyLoss()

num_epochs = 10
lr = 0.1
d2l.train_ch3(net, train_iter, test_iter, loss, num_epochs, batch_size, lr)

