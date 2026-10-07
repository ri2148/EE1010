#Code by Arjun
#Date:07=-10-26

import matplotlib.pyplot as plt
import numpy as np
import subprocess
import shlex

# 1. Calculate values of 'a' and 'b' using analytical derivatives
# Right-hand function: f(x) = x^3 + x^2 + 1 for x >= 1
def f_right(x):
    return x**3 + x**2 + 1


# Derivative of right-hand function: f'(x) = 3*x^2 + 2*x
def df_right(x):
    return 3 * x**2 + 2 * x


x_boundary = 1.0

# Differentiability at x = 1: slope 'a' of (ax + b) equals f'(1)
a_val = df_right(x_boundary)

# Continuity at x = 1: a*(1) + b = f(1) => b = f(1) - a
b_val = f_right(x_boundary) - a_val * x_boundary

print(f"Calculated values: a = {a_val}, b = {b_val}")


# 2. Plotting setup
x_left = np.linspace(-1, 1, 300)
x_right = np.linspace(1, 2.5, 300)

y_left = a_val * x_left + b_val
y_right = f_right(x_right)

# Extended tangent line
x_full = np.linspace(-1, 2.5, 600)
y_tangent = a_val * x_full + b_val

plt.figure(figsize=(8, 6))
plt.plot(
    x_left,
    y_left,
    "b-",
    linewidth=2.5,
    label=f"$f(x) = {int(a_val)}x {int(b_val):+d}$ ($x < 1$)",
)
plt.plot(
    x_right,
    y_right,
    "r-",
    linewidth=2.5,
    label="$f(x) = x^3 + x^2 + 1$ ($x \\geq 1$)",
)
plt.plot(
    x_full,
    y_tangent,
    "k--",
    alpha=0.6,
    label=f"Tangent Line ($y = {int(a_val)}x {int(b_val):+d}$)",
)

# Point of tangency (1, 3)
plt.scatter(
    [x_boundary],
    [f_right(x_boundary)],
    color="black",
    zorder=5,
    label=f"Point of Tangency (1, {int(f_right(x_boundary))})",
)

plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.axvline(0, color="gray", linestyle=":", linewidth=0.8)
plt.axhline(0, color="gray", linestyle=":", linewidth=0.8)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)

plt.savefig("Plot.pdf")
subprocess.run(shlex.split("termux-open Plot.pdf"))

