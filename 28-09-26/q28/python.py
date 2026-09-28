import numpy as np
import matplotlib.pyplot as plt
import subprocess 
import shlex

# Define coefficient matrix A and constants vector B
A = np.array([[1, 1],
              [3, 1]])
B = np.array([7, 13])

# Method 1: Direct matrix inverse (X = A^-1 * B)
A_inv = np.linalg.inv(A)
X_inv = np.dot(A_inv, B)

# Method 2: Direct linear solver
X_solve = np.linalg.solve(A, B)

x_val, y_val = X_solve[0], X_solve[1]
print(f"Solution: x = {x_val:.1f}, y = {y_val:.1f}")

# Plotting the lines
x = np.linspace(-1, 8, 400)
y1 = 7 - x
y2 = 13 - 3 * x

plt.figure(figsize=(8, 6))
plt.plot(x, y1, label='x + y = 7 (y = 7 - x)', color='#1f77b4', linewidth=2)
plt.plot(x, y2, label='3x + y = 13 (y = 13 - 3x)', color='#d62728', linewidth=2)

# Highlight intersection point
plt.plot(x_val, y_val, 'go', markersize=9, label=f'Intersection ({x_val:.1f}, {y_val:.1f})')
plt.annotate(f'({x_val:.1f}, {y_val:.1f})', 
             xy=(x_val, y_val), 
             xytext=(x_val + 0.5, y_val + 1),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=6),
             fontsize=12, fontweight='bold')

plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.xlim(-1, 7)
plt.ylim(-1, 10)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('Intersection of Lines: x + y = 7 and 3x + y = 13', fontsize=14)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(fontsize=11)
plt.savefig("Plot.pdf")
subprocess.run(shlex.split("termux-open Plot.pdf"))
