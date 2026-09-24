#code by arjun
#24-09-2026

import numpy as np

# 1.Define Matrix P
P = np.array([
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
], dtype=float)

# Compute Trace, Transpose, and Eigenvalues
trace_P = np.trace(P)
eigenvalues = np.linalg.eigvals(P)
sum_eigenvalues = np.sum(eigenvalues)

print(f"Matrix P:\n{P}\n")
print(f"1. Trace of P: {trace_P}")
print(f"   Eigenvalues of P: {eigenvalues}")
print(f"   Sum of Eigenvalues: {sum_eigenvalues}")

# Option (A) Verification
is_option_A_true = np.isclose(trace_P, sum_eigenvalues)
print(f"Option (A) [Trace = Sum of Eigenvalues]: {is_option_A_true}\n")

# Option (B) Verification: P^T * P == Identity Matrix?
P_T_P = P.T @ P
identity_3x3 = np.eye(3)
is_option_B_true = np.allclose(P_T_P, identity_3x3)
print(f"2. P^T * P:\n{P_T_P}")
print(f"Option (B) [P^T * P is Identity]: {is_option_B_true}\n")

# Option (C) Verification: P^T == -P?
is_option_C_true = np.allclose(P.T, -P)
print(f"3. Transpose P^T:\n{P.T}")
print(f" -P:\n{-P}")
print(f"Option (C) [P is Skew-Symmetric]: {is_option_C_true}\n")

# Option (D) Verification: Absolute magnitude of each eigenvalue is 1?
abs_eigenvalues = np.abs(eigenvalues)
is_option_D_true = np.all(np.isclose(abs_eigenvalues, 1.0))
print(f"4. Absolute Magnitudes of Eigenvalues: {abs_eigenvalues}")
print(f"Option (D) [Absolute Magnitude of each Eigenvalue is 1]: {is_option_D_true}\n")

