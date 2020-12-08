import random
import numpy as np

random.seed()

A = np.random.rand(3, 3) * 10

det = np.linalg.det(A)

print(A, "\n")
print(det)
