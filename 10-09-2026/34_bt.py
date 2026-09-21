#code by Arjun
#Date:10-09-2026

import numpy as np
import matplotlib.pyplot as plt
import subprocess
import shlex
matrix = np.array([
    [2.0, 3.0, 6.0, 0.0],
    [4.0, 6.0, 0.0, 3.0]
])

#Row Operation: R2 -> R2 - 2*R1
matrix[1] = matrix[1] - 2 * matrix[0]

#Display transformed matrix
print("Matrix after operation (R2 -> R2 - 2*R1):")
print(f"[{matrix[0, 0]:.0f}  {matrix[0, 1]:.0f} :  {matrix[0, 2]:.0f}]")
print(f"[{matrix[1, 0]:.0f}  {matrix[1, 1]:.0f} :  3k - 12]\n")


# Solve for infinite solutions automatically: 3k - 12 = 0
const_term = matrix[1, 2]  # -12.0
k_coeff = matrix[1, 3]     # 3.0

# 3k - 12 = 0  =>  3k = 12  =>  k = 12 / 3
k_auto = -const_term / k_coeff

print(f"For infinite solutions:")
print(f"{k_coeff:.0f}k - {abs(const_term):.0f} = 0")
print(f"{k_coeff:.0f}k = {abs(const_term):.0f}")
print(f"k = {int(k_auto)}\n")

# --- OPTION TO INPUT k MANUALLY ---
user_input = input("Enter a value for k (or press Enter to use the computed k): ").strip()

if user_input:
    k = float(user_input)
else:
    k = k_auto

print(f"\nEvaluating system for k = {k}:")

# --- DEFINE ORIGINAL UN-REDUCED EQUATIONS ---
# Line 1: 2x + 3y = 6
a1, b1, c1 = 2.0, 3.0, 6.0 

# Line 2 (Original equation before row reduction): 2x + 3y = 3k/2
a2, b2 = 2.0, 3.0 
c2 = 1.5 * k 
#To check for state of system
A = np.array([[a1, b1, c1], [a2, b2, c2]], dtype=float)

if abs(A[0, 0]) > 1e-9:
    factor = A[1, 0] / A[0, 0]
    A[1] = A[1] - factor * A[0]

if abs(A[1, 0]) < 1e-9 and abs(A[1, 1]) < 1e-9:
    if abs(A[1, 2]) < 1e-9:
        print(f"-> Infinite solutions for k = {k}! (Lines coincide)")
    else:
        print(f"-> No solution for k = {k}! (Lines are parallel)")
else:
    y_sol = A[1, 2] / A[1, 1]
    x_sol = (A[0, 2] - A[0, 1] * y_sol) / A[0, 0]
    print(f"-> Unique solution: x = {x_sol:.2f}, y = {y_sol:.2f}")
# --- MATGEO UTILITY FUNCTION ---
def line_dir_pt(m, A, k1=-10, k2=10):
    length = 100
    dim = A.shape[0]
    x_line = np.zeros((dim, length))
    lam = np.linspace(k1, k2, length)
    for i in range(length):
        temp1 = A + lam[i] * m
        x_line[:, i] = temp1.T
    return x_line

# --- PLOTTING LOGIC USING MATGEO TEMPLATE ---
plt.figure(figsize=(8, 6))

# Line 1: Direction vector m1 = [-b1, a1]^T, Point A1 = [0, c1/b1]^T
m1 = np.array([[-b1], [a1]], dtype=float)
A1 = np.array([[0.0], [c1 / b1]], dtype=float) if abs(b1) > 1e-9 else np.array([[c1 / a1], [0.0]], dtype=float)
x_line1 = line_dir_pt(m1, A1)

plt.plot(x_line1[0, :], x_line1[1, :], label=f'Line 1: {a1:.0f}x + {b1:.0f}y = {c1:.0f}', color='blue', linewidth=2.5)

# Line 2: Direction vector m2 = [-b2, a2]^T, Point A2 = [0, c2/b2]^T
m2 = np.array([[-b2], [a2]], dtype=float)
A2 = np.array([[0.0], [c2 / b2]], dtype=float) if abs(b2) > 1e-9 else np.array([[c2 / a2], [0.0]], dtype=float)
x_line2 = line_dir_pt(m2, A2)

plt.plot(x_line2[0, :], x_line2[1, :], label=f'Line 2: {a2:.0f}x + {b2:.0f}y = {c2:.1f}', color='red', linestyle='--', linewidth=2)

# Mark Intersection if a unique solution exists
if not (abs(A[1, 0]) < 1e-9 and abs(A[1, 1]) < 1e-9):
    plt.scatter(x_sol, y_sol, color='green', s=80, zorder=5, label=f'Intersection ({x_sol:.2f}, {y_sol:.2f})')

plt.axhline(0, color='black', linewidth=0.8, linestyle=':')
plt.axvline(0, color='black', linewidth=0.8, linestyle=':')
plt.grid(True, linestyle='--', alpha=0.6)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title(f'System Visualizer (k = {k})')
plt.axis('equal')
plt.legend()
plt.savefig("BT_34.pdf")
subprocess.run(shlex.split("termux-open BT_34.pdf"))
