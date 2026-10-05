import matplotlib.pyplot as plt
import numpy as np
import subprocess
import shlex
# Define x domains
x_left = np.linspace(-1, 1, 300)
x_right = np.linspace(1, 2.5, 300)

# Constants for differentiability
a, b = 5, -2

# Piecewise function evaluations
y_left = a * x_left + b
y_right = x_right**3 + x_right**2 + 1

# Tangent line extended across the full domain to illustrate smoothness at x = 1
x_full = np.linspace(-1, 2.5, 600)
y_tangent = 5 * x_full - 2

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(x_left, y_left, "b-", linewidth=2.5, label="$f(x) = 5x - 2$ ($x < 1$)")
plt.plot(
    x_right,
    y_right,
    "r-",
    linewidth=2.5,
    label="$f(x) = x^3 + x^2 + 1$ ($x \geq 1$)",
)
plt.plot(
    x_full,
    y_tangent,
    "k--",
    alpha=0.6,
    label="Common Tangent Line ($y = 5x - 2$)",
)

# Highlight the transition point x = 1
plt.scatter([1], [3], color="black", zorder=5, label="Point of Tangency $(1, 3)$")

plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.axvline(0, color="gray", linestyle=":", linewidth=0.8)
plt.axhline(0, color="gray", linestyle=":", linewidth=0.8)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)

plt.savefig("Plot.pdf")
subprocess.run(shlex.split("termux-open Plot.pdf"))
