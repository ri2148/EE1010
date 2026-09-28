import numpy as np

# One-line Cholesky decomposition using NumPy
L = np.linalg.cholesky([[9, 15], [15, 50]])

# Accessing |l_22| (which is L[1, 1]):
print("Required value is:")
print(abs(L[1, 1]))  # Output: 5.0

