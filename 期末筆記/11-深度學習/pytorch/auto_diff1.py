# 來源 -- https://github.com/dsgiitr/d2l-pytorch/blob/master/Ch04_The_Preliminaries_A_Crashcourse/Automatic_Differentiation.ipynb
import torch
from torch.autograd import Variable

x = Variable(torch.arange(4, dtype=torch.float32).reshape((4, 1)), requires_grad=True)
print(x)

y = 2*torch.mm(x.t(),x)
print(y)

y.backward()


print("x.grad:", x.grad)
print("x.grad_fn:", x.grad_fn)
print("y.grad_fn:", y.grad_fn)

print((x.grad - 4*x).norm().item() == 0)
print(x.grad)
