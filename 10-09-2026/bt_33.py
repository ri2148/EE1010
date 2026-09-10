import numpy as np
import matplotlib.pyplot as plt
import subprocess
import shlex
# Define x range and function
x = np.linspace(-1, 2, 400)
y = np.exp(x) - 2

# Plot setup
plt.figure(figsize=(8, 4.5))
plt.plot(x, y, label=r'$f(x) = e^x - 2$', color='#1f77b4', linewidth=2)

# Reference axes (x=0, y=0)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')

# Labels and styling
plt.title(r'Plot of $f(x) = e^x - 2$', fontsize=12)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.tight_layout()

plt.savefid("BT_33.PNG")
subprocess.run(shlex.split("termux-open BT_33.pdf"))

