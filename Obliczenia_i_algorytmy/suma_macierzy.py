import random
import numpy as np

random.seed()

A = np.random.rand(128, 128) * 100
B = np.random.rand(128, 128) * 100

C = A + B

print("{:.2f}".format(A[0][0]), "\t", "{:.2f}".format(A[1][1]), "\t", "{:.2f}".format(A[2][2]), "\n")
print("{:.2f}".format(B[0][0]), "\t", "{:.2f}".format(B[1][1]), "\t", "{:.2f}".format(B[2][2]), "\n")
print("{:.2f}".format(C[0][0]), "\t", "{:.2f}".format(C[1][1]), "\t", "{:.2f}".format(C[2][2]), "\n")
