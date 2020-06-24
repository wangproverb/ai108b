import numpy as np
from numpy import linalg as LA

A = np.array([[4,3,6],[1,1,2],[2,1,3]])
B = np.array([[1,2,-1]]).transpose()
C = A.dot(B)
D = C-B
n = LA.norm(C, 2)

print('A.shape[0]=', A.shape[0])

print(A)
print(B)
print(C)
print(D)
print(n)