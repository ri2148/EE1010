import matplotlib.pyplot as plt
import numpy as np
import subprocess
import shlex

#Generate Uniform random variables 
num_samples = 1000
U = np.random.uniform(0, 1, num_samples)

#Transform U to X:X = (63U + 1)^(1/3)
X = (63 * U + 1) ** (1 / 3)

#Empirical CDF
sorted_X = np.sort(X)
y_empirical = np.arange(1, num_samples + 1) / num_samples

#Theoretical CDF
x_vals = np.linspace(0.5, 4.5, 1000)
y_theoretical = np.clip((x_vals**3 - 1) / 63, 0, 1)

#pLot
plt.figure(figsize=(8, 5))
plt.plot(
    sorted_X,
    y_empirical,
    color="blue",
    lw=2.5,
    label="Empirical CDF (Simulated)",
)
plt.plot(
    x_vals,
    y_theoretical,
    "r--",
    lw=2,
    label=r"Theoretical CDF: $F(x) = \frac{x^3 - 1}{63}$",
)

plt.title("Cumulative Distribution Function (CDF)")
plt.xlabel("x")
plt.ylabel("F(x)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("Randomvar.pdf")
subprocess.run(shlex.split("termux-open Randomvar.pdf"))
