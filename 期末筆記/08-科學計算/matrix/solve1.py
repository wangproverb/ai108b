import numpy as np
from scipy import linalg

m,n=500,50

A = np.random.rand(m, m)
B = np.random.rand(m, n)
X1 = linalg.solve(A,B)
X2 = np.dot(linalg.inv(A), B)

print(np.allclose(X1,X2))

# %timeit linalg.solve(A,B)
# %timeit np.dot(linalg.inv(A), B)
