import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import subprocess
import shlex
#calculating values of 'a' and 'b'
x, a, b = sp.symbols("x a b")

#Define the right-side function for x >= 1
f_right = x**3 + x**2 + 1
df_right = sp.diff(f_right, x)

#Differentiability requirement at x = 1: f_left'(1) = f_right'(1)
#f_left'(x) = d/dx (ax + b) = a
a_val = float(df_right.subs(x, 1))

#Continuity requirement at x = 1: f_left(1) = f_right(1)
# f_left(1) = a*(1) + b => b = f_right(1) - a
f_right_at_1 = float(f_right.subs(x, 1))
b_val = f_right_at_1 - a_val

print(f"Calculated constants: a = {a_val}, b = {b_val}")

#Plotting the piecewise function and tangent line
x_left = np.linspace(-1, 1, 300)
x_right = np.linspace(1, 2.5, 300)

y_left = a_val * x_left + b_val
y_right = x_right**3 + x_right**2 + 1

#Tangent line extended across the full range
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

#Highlighting the boundary point (1, 3)
plt.scatter(
    [1],
    [f_right_at_1],
    color="black",
    zorder=5,
    label=f"Point of Tangency $(1, {int(f_right_at_1)})$",
)

plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.axvline(0, color="gray", linestyle=":", linewidth=0.8)
plt.axhline(0, color="gray", linestyle=":", linewidth=0.8)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)

plt.savefig("Plot.pdf")
subprocess.run(shlex.split("termux-open Plot.pdf"))
