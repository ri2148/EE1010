#code by arjun, 05-10-26

import numpy as np
import matplotlib.pyplot as plt
import subprocess
import shlex
#Function to solve sytem
def solve_system(k):
    A = np.array([[1, k], [k, 1]])
    B = np.array([1, -1])
    
    det = np.linalg.det(A)
    # Augmented matrix determinant check for consistency
    aug = np.column_stack((A, B))
    rank_A = np.linalg.matrix_rank(A)
    rank_aug = np.linalg.matrix_rank(aug)
    
    if rank_A == rank_aug:
        if rank_A == 2:
            sol = np.linalg.solve(A, B)
            return f"Unique solution: x = {sol[0]:.2f}, y = {sol[1]:.2f}"
        else:
            return "Infinitely many solutions"
    else:
        return "No solution"
# 1. Verification Outputs
print("--- Verification Results ---")
for k_val in [1, -1, 2]:
    print(f"k = {k_val:2d} -> {solve_system(k_val)}")

# 2. Plotting the Lines
k_values = [1, -1, 2]
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
x = np.linspace(-5, 5, 400)

for ax, k in zip(axes, k_values):
    if k == 1:
        # Line 1: x + y = 1  => y = 1 - x
        # Line 2: x + y = -1 => y = -1 - x
        y1 = 1 - x
        y2 = -1 - x
        title = "k = 1 (No Solution / Parallel Lines)"
    elif k == -1:
        # Line 1: x - y = 1   => y = x - 1
        # Line 2: -x + y = -1 => y = x - 1
        y1 = x - 1
        y2 = x - 1
        title = "k = -1 (Infinitely Many Solutions / Coincident Lines)"
    else:
        # General Unique Case (e.g., k = 2)
        y1 = (1 - x) / k
        y2 = -1 - k * x
        title = f"k = {k} (Unique Solution)"

    ax.plot(x, y1, label=f"Line 1 (x + {k}y = 1)", color="blue", linewidth=2)
    ax.plot(x, y2, label=f"Line 2 ({k}x + y = -1)", color="orange", linestyle="--" if k == -1 else "solid", linewidth=2)
    
    ax.axhline(0, color="black", linewidth=0.5)
    ax.axvline(0, color="black", linewidth=0.5)
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.set_title(title, fontsize=11, fontweight="bold")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)

plt.tight_layout()
plt.savefig("Plot.pdf")
subprocess.run(shlex.split("termux-open Plot.pdf"))
