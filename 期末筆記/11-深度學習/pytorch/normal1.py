from matplotlib import pyplot as plt
from IPython import display
import torch
import math

x = torch.arange(-7, 7, 0.01)
# Mean and variance pairs
parameters = [(0,1), (0,2), (3,1)]

# Display SVG rather than JPG
display.set_matplotlib_formats('svg')
plt.figure(figsize=(10, 6))
for (mu, sigma) in parameters:
    p = (1/math.sqrt(2 * math.pi * sigma**2)) * torch.exp(-(0.5/sigma**2) * (x-mu)**2)
    plt.plot(x.numpy(), p.numpy(), label='mean ' + str(mu) + ', variance ' + str(sigma))

plt.legend()
plt.show()
