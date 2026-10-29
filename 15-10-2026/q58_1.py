import shlex
import subprocess
import matplotlib.pyplot as plt
import numpy as np

# Set a smaller sample size so individual stems are visible in the plot
num_samples = 50

# 1. Generate Uniform random variables U ~ Uniform(0, 1)
U = np.random.uniform(0, 1, num_samples)

# 2. Transform U to X: X = (63U + 1)^(1/3)
X = (63 * U + 1) ** (1 / 3)

# 3. Create Stem Plot
plt.figure(figsize=(10, 5))
sample_indices = np.arange(1, num_samples + 1)

markerline, stemlines, baseline = plt.stem(
    sample_indices, X, linefmt="b-", markerfmt="bo", basefmt="r-"
)
plt.setp(markerline, markersize=4)

plt.title(
    r"Stem Plot of Generated Random Variables $X = (63U + 1)^{1/3}$",
    fontsize=12,
)
plt.xlabel("Sample Index ($n$)")
plt.ylabel("Generated Value ($X_n$)")
plt.ylim(0, 4.5)  # Range bounds for the distribution [1, 4]
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()

# Save and open in Termux
plt.savefig("Randomvar.pdf")
subprocess.run(shlex.split("termux-open Randomvar.pdf"))

