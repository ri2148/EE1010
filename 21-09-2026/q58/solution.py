#code by arjun
#date : 21-09-2026

import numpy as np

# Coefficient matrix A (4 rows x 3 columns)
A = np.array([
    [1.0, 1.0, 0.0],   # Carbon:   1a   + 1b + 0c = 6
    [18.0, 0.0, 3.0],  # Hydrogen: 18a  + 0b + 3c = 15
    [0.5, 2.0, 0.0],   # Oxygen:   0.5a + 2b + 0c = 8
    [0.2, 0.0, 1.0]    # Nitrogen: 0.2a + 0b + 1c = 1
])

# Constants vector b
b = np.array([6.0, 15.0, 8.0, 1.0])

# Solve overdetermined system using Least Squares
x, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)

a, b_val, c = x

print(f"a = {a:.4f}")
print(f"b = {b_val:.4f}")
print(f"c = {c:.4f}")

