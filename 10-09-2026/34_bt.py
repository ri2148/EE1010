#code by Arjun
#date:10-09-2026
#using gauss elimination
import numpy as np
import matplotlib.pyplot as plt
import subprocess
import shlex
#Defining initial augmented matrix tracking coefficients: [x, y, constant, k_coeff]
#Row 1: 2x + 3y = 6  -> [2, 3, 6, 0]
#Row 2: 4x + 6y = 3k -> [4, 6, 0, 3]
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

#Solve for infinite solutions: 3k - 12 = 0
const_term = matrix[1, 2]  # -12.0
k_coeff = matrix[1, 3]     # 3.0

#3k - 12 = 0  =>  3k = 12  =>  k = 12 / 3
k = -const_term / k_coeff

print(f"For infinite solutions:")
print(f"{k_coeff:.0f}k - {abs(const_term):.0f} = 0")
print(f"{k_coeff:.0f}k = {abs(const_term):.0f}")
print(f"k = {int(k)}")
#--- OPTION TO INPUT k MANUALLY ---
user_input = input("Enter a value for k (or press Enter to use the computed k): ").strip()

if user_input:
    k = float(user_input)
else:
    k = k_auto

print(f"\nEvaluating system for k = {k}:")

# --- DEFINE ORIGINAL UN-REDUCED EQUATIONS ---
# Line 1: 2x + 3y = 6
a1, b1, c1 = 2.0, 3.0, 6.0 

# Line 2 (Original equation before row reduction): 2x + 3y = 3k
a2, b2 = 2.0, 3.0 
c2 = 3.0 * k 

# --- EVALUATE SYSTEM STATE ---
det = a1 * b2 - a2 * b1  # Determinant (0 means parallel or identical)

if abs(det) < 1e-9:
    if abs(a1 * c2 - a2 * c1) < 1e-9:
        print(f"-> Infinite solutions for k = {k}! (Lines coincide)")
    else:
        print(f"-> No solution for k = {k}! (Lines are parallel)")
else:
    x_sol = (c1 * b2 - b1 * c2) / det
    y_sol = (a1 * c2 - c1 * a2) / det
    print(f"-> Unique solution: x = {x_sol:.2f}, y = {y_sol:.2f}")

# --- PLOTTING BOTH ORIGINAL LINES ---
x_vals = np.linspace(-10, 10, 400)
plt.figure(figsize=(8, 6))

# Line 1 (Solid Blue)
y_vals1 = (c1 - a1 * x_vals) / b1
plt.plot(x_vals, y_vals1, label=f'Line 1: {a1:.0f}x + {b1:.0f}y = {c1:.0f}', color='blue', linewidth=2.5)

# Line 2 (Dashed Red)
y_vals2 = (c2 - a2 * x_vals) / b2
plt.plot(x_vals, y_vals2, label=f'Line 2: {a2:.0f}x + {b2:.0f}y = {c2/2:.1f}', color='red', linestyle='--', linewidth=2)

# Mark Intersection if lines cross
if abs(det) >= 1e-9:
    plt.plot(x_sol, y_sol, 'go', markersize=9, zorder=5, label=f'Intersection ({x_sol:.2f}, {y_sol:.2f})')

plt.axhline(0, color='black', linewidth=0.8, linestyle=':')
plt.axvline(0, color='black', linewidth=0.8, linestyle=':')
plt.grid(True, linestyle='--', alpha=0.6)
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'System Visualizer (k = {k})')
plt.legend()
plt.savefig("BT_34.pdf")
subprocess.run(shlex.split("termux-open BT_34.pdf"))
