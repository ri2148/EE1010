import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import subprocess
import shlex
# 1. Define a uniform meshgrid over (x1, x2) for consistent surface plotting
x1_vals = np.linspace(-5, 5, 50)
x2_vals = np.linspace(-5, 5, 50)
X1, X2 = np.meshgrid(x1_vals, x2_vals)

# 2. Equation of Plane 1: x1 + x2 + x3 = 0  =>  x3 = -x1 - x2
X3_plane1 = -X1 - X2

# 3. Equation of Plane 2: x1 + 2*x3 = 0  =>  x3 = -0.5 * x1
# (Note: x2 is free to vary across X2)
X3_plane2 = -0.5 * X1

# 4. Parametric equation of the Line of Intersection:
# x1 = -2*t, x2 = t, x3 = t
t = np.linspace(-4, 4, 100)
x1_line = -2 * t
x2_line = 1 * t
x3_line = 1 * t

# 5. Plotting setup
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Surface plot for Plane 1 (Cyan)
ax.plot_surface(X1, X2, X3_plane1, alpha=0.45, color='cyan', edgecolor='none')

# Surface plot for Plane 2 (Orange)
ax.plot_surface(X1, X2, X3_plane2, alpha=0.45, color='orange', edgecolor='none')

# Line of Intersection (Red)
ax.plot(x1_line, x2_line, x3_line, color='red', linewidth=3.5)

# Labeling and Axis limits
ax.set_xlabel('X1 Axis')
ax.set_ylabel('X2 Axis')
ax.set_zlabel('X3 Axis')
ax.set_title('3D Intersection of Planes (GATE CE Q12)')

ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([-5, 5])

# Set camera angle to clearly show both intersecting surfaces
ax.view_init(elev=25, azim=135)

# Custom Legend
legend_elements = [
    Line2D([0], [0], color='cyan', lw=4, alpha=0.5, label='Plane 1: x1 + x2 + x3 = 0'),
    Line2D([0], [0], color='orange', lw=4, alpha=0.5, label='Plane 2: x1 + 2*x3 = 0'),
    Line2D([0], [0], color='red', lw=3.5, label='Line of Intersection')
]
ax.legend(handles=legend_elements, loc='upper left')

plt.tight_layout()

plt.savefig("Plot.pdf")
subprocess.run(shlex.split("termux-open Plot.pdf"))
