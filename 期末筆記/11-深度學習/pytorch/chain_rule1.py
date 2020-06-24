import torch
from torch.autograd import Variable


x = Variable(torch.tensor([[0.],[1.],[2.],[3.]]), requires_grad=True)
y = x * 2
z = y * x

head_gradient = torch.tensor([[10], [1.], [.1], [.01]])
z.backward(head_gradient)
print(x.grad)