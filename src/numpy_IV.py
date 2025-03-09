import numpy as np
import numpy.linalg as linalg

rand = np.random.default_rng(1997)
A = rand.integers(0, 5, (3, 3))
B = rand.integers(0, 5, (3, 3))
y = rand.integers(0, 5, (3, 1))

print("A\n", A)
print("B\n", B)
print("A + B\n", A + B)
print("A - B\n", A - B)
print("A * B\n", A * B)
print("A / B\n", A / B)

print("A.dot(B)\n", A.dot(B))
