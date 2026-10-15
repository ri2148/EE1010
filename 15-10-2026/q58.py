import numpy as np
import matplotlib.pyplot as plt
import subprocess
import shlex

# 1. Define CDF parameters
def theoretical_cdf(x):
    # F(x) = (x^3 - 1) / 63 clipped between [0, 1]
    return np.clip((x**3 - 1) / 63, 0, 1)

# 2. Inverse Transform Sampling (generate random variables)
def sample_custom_pdf(num_samples):
    u = np.random.uniform(0, 1, num_samples)
    return (63 * u + 1) ** (1 / 3)

# 3. Generate simulation data
num_samples = 100000
samples = sample_custom_pdf(num_samples)

# 4. Compute Empirical CDF from samples
sorted_samples = np.sort(samples)
y_empirical = np.arange(1, num_samples + 1) / num_samples

# 5. Theoretical CDF points
x_vals = np.linspace(0, 5, 1000)
y_theoretical = theoretical_cdf(x_vals)

# 6. Plotting
plt.figure(figsize=(8, 5))

# Plot Empirical CDF
plt.plot(sorted_samples, y_empirical, color='blue', lw=2.5, label='Empirical CDF (Simulated)')

# Plot Theoretical CDF
plt.plot(x_vals, y_theoretical, 'r--', lw=2, label='Theoretical CDF: F(x) = (x^3 - 1)/63')

plt.title('Cumulative Distribution Function (CDF)')
plt.xlabel('x')
plt.ylabel('F(x)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

# Save plot to file (works reliably in headless / Termux environments)
plt.tight_layout()
plt.savefig('cdf_plot.pdf')
subprocess.run(shlex.split("termux-open cdf_plot.pdf"))
