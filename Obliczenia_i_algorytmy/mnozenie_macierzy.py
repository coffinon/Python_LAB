import random
import numpy as np

random.seed()

A = np.random.rand(8, 8) * 100
B = np.random.rand(8, 8) * 100

C = np.matmul(A, B)

print(A, "\n")
print(B, "\n")
print(C, "\n")
