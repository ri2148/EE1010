import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import subprocess
import shlex

# 1. Define a grid of points for x1 and x3
x1_vals = np.linspace(-5, 5, 50)
x3_vals = np.linspace(-5, 5, 50)
X1, X3 = np.meshgrid(x1_vals, x3_vals)

# 2. Equation of Plane 1: x1 + x2 + x3 = 0  =>  x2 = -x1 - x3
X2_plane1 = -X1 - X3

# 3. Equation of Plane 2: x1 + 2*x3 = 0
x2_vals = np.linspace(-5, 5, 50)
X2_p2, X3_p2 = np.meshgrid(x2_vals, x3_vals)
X1_plane2 = -2 * X3_p2

# 4. Parametric equation of the Line of Intersection
t = np.linspace(-5, 5, 100)
x1_line = -2 * t
x2_line = 1 * t
x3_line = 1 * t

# 5. Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Surface plot for Plane 1
ax.plot_surface(X1, X2_plane1, X3, alpha=0.5, color='cyan', edgecolor='none')

# Surface plot for Plane 2
ax.plot_surface(X1_plane2, X2_p2, X3_p2, alpha=0.5, color='orange', edgecolor='none')

# Plot the Line of Intersection
ax.plot(x1_line, x2_line, x3_line, color='red', linewidth=3.5)

# Labeling and Formatting
ax.set_xlabel('X1 Axis')
ax.set_ylabel('X2 Axis')
ax.set_zlabel('X3 Axis')
ax.set_title('3D Intersection of Planes (GATE CE Q12)')

# Custom Legend Handles (Fixes the AttributeError)
legend_elements = [
    Line2D([0], [0], color='cyan', lw=4, alpha=0.5, label='Plane 1: x1 + x2 + x3 = 0'),
    Line2D([0], [0], color='orange', lw=4, alpha=0.5, label='Plane 2: x1 + 2*x3 = 0'),
    Line2D([0], [0], color='red', lw=3.5, label='Line of Intersection')
]
ax.legend(handles=legend_elements)


plt.savefig("Plot.pdf")
subprocess.run(shlex.split("termux-open Plot.pdf"))
