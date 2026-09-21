import matplotlib.pyplot as plt
import numpy as np
import subprocess
import shlex
# Constants determined for differentiability/continuity
a = 0
b = 2

# Domain ranges
x_left = np.linspace(-1.5, 0, 200)
x_right = np.linspace(0, 1.5, 200)

# Function definitions
y_left = a + b * x_left  # f(x) = 2x
y_right = np.sin(2 * x_right)  # f(x) = sin(2x)

# Plotting setup
plt.figure(figsize=(8, 5))

# Plot left and right branches
plt.plot(x_left, y_left, label=r"$f(x) = 2x$ ($x \leq 0$)", color="crimson", lw=2)
plt.plot(
    x_right, y_right, label=r"$f(x) = \sin(2x)$ ($x > 0$)", color="dodgerblue", lw=2
)

# Highlight point of continuity at x = 0
plt.plot(
    0,
    0,
    marker="o",
    markersize=8,
    color="black",
    label=r"Point of Continuity/Differentiability $(0, 0)$",
)

# Graph styling
plt.axhline(0, color="gray", linewidth=0.8, linestyle="--")
plt.axvline(0, color="gray", linewidth=0.8, linestyle="--")
plt.title(
    r"Piecewise Function $f(x)$ showing Continuity & Differentiability at $x=0$",
    fontsize=12,
)
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="upper left")

plt.savefig("BT-46.pdf")
subprocess.run(shlex.split("termux-open BT-46.pdf"))

