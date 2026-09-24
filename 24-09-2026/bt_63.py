#Code by Arjun
#date:24-09-2026

import numpy as np

#Given eigenvalues from the problem
given_eigenvalues = np.array([-2, 1, 2])

#We know that trace(A) = sum of eigenvalues
#Trace = 1 + k + (-1) = k
k = np.sum(given_eigenvalues)

#Constructing matrix
A = np.array([
    [1, 0, 1],
    [0, k, 0],
    [3, 0, -1]
], dtype=float)

#Verifying by computing eigenvalues with numpy
computed_eigenvalues = np.sort(np.linalg.eigvals(A))
expected_eigenvalues = np.sort(target_eigenvalues)

print(f"Calculated k: {int(k)}")
print(f"Computed eigenvalues for k={int(k)}: {computed_eigenvalues}")
print(f"Match expected: {np.allclose(computed_eigenvalues, expected_eigenvalues)}") #To check if matching 

