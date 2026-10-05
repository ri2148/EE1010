#code by arjun, 05-10-26
import numpy as np
import matplotlib.pyplot as plt
import subprocess
import shlex

#To get row reduced form
def get_rref(matrix):
    A = matrix.copy().astype(float)
    
    #Clean up small floating point numbers near zero
    A[np.abs(A) < 1e-12] = 0.0

    # Step 1: Normalize Row 1 if possible
    if A[0, 0] != 0:
        A[0] = A[0] / A[0, 0]
        # Eliminate variable 1 from Row 2
        A[1] = A[1] - A[1, 0] * A[0]
    elif A[1, 0] != 0: # Swap rows if first element is 0
        A[[0, 1]] = A[[1, 0]]
        A[0] = A[0] / A[0, 0]
        A[1] = A[1] - A[1, 0] * A[0]

    A[np.abs(A) < 1e-12] = 0.0

    # Step 2: Normalize Row 2 if possible
    if A[1, 1] != 0:
        A[1] = A[1] / A[1, 1]
        # Eliminate variable 2 from Row 1
        A[0] = A[0] - A[0, 1] * A[1]

    A[np.abs(A) < 1e-12] = 0.0
    return A

def analyze_and_plot():
    # 1. Get user input
    k_val = float(input("Enter the value of k: "))

    # 2. Build Augmented Matrix [1 k | 1; k 1 | -1]
    aug_matrix = np.array([
        [1.0, k_val, 1.0],
        [k_val, 1.0, -1.0]
    ])

    rref_matrix = get_rref(aug_matrix)

    print("\n" + "=" * 40)
    print(f"RESULTS FOR k = {k_val}")
    print("=" * 40)
    print("Final Row Reduced Echelon Form (RREF):")
    print(np.array2string(rref_matrix, formatter={'float_kind': lambda x: f"{x:7.2f}"}))
    print("-" * 40)

    # 3. Check consistency and solution type using matrix ranks
    A = aug_matrix[:, :2]
    B = aug_matrix[:, 2]
    
    rank_A = np.linalg.matrix_rank(A)
    rank_aug = np.linalg.matrix_rank(aug_matrix)

    if rank_A < rank_aug:
        status = "No Solution (Parallel Lines)"
        print(f"Status: {status}")
    elif rank_A == rank_aug < 2:
        status = "Infinitely Many Solutions (Coincident Lines)"
        print(f"Status: {status}")
    else:
        sol = np.linalg.solve(A, B)
        status = f"Unique Solution: x = {sol[0]:.4f}, y = {sol[1]:.4f}"
        print(f"Status: {status}")
# 4. Generate Single Plot
    plt.figure(figsize=(7, 6))
    x = np.linspace(-5, 5, 400)

    # Line 1: x + k*y = 1
    if k_val != 0:
        y1 = (1 - x) / k_val
        plt.plot(x, y1, label=f"Line 1: x + {k_val:.1f}y = 1", color="blue", linewidth=2)
    else:
        plt.axvline(x=1, label="Line 1: x = 1", color="blue", linewidth=2)

    # Line 2: k*x + y = -1  =>  y = -1 - k*x
    y2 = -1 - k_val * x
    plt.plot(x, y2, label=f"Line 2: {k_val:.1f}x + y = -1", color="orange", 
             linestyle="--" if k_val == -1 else "solid", linewidth=2)

    # Intersection point (if unique solution exists)
    if rank_A == rank_aug == 2:
        plt.plot(sol[0], sol[1], 'ro', markersize=8, zorder=5,
                 label=f"Intersection ({sol[0]:.2f}, {sol[1]:.2f})")

    plt.axhline(0, color="black", linewidth=0.8)
    plt.axvline(0, color="black", linewidth=0.8)
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.title(f"System of Linear Equations for k = {k_val}\n({status})", fontsize=11, fontweight="bold")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.legend(loc="upper right")
    plt.tight_layout()
    plt.savefig("PLot.pdf")
    subprocess.run(shlex.split("termux-open PLot.pdf"))

if __name__ == "__main__":
    analyze_and_plot()

