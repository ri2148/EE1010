import numpy as np
import matplotlib.pyplot as plt
import subprocess
import shlex

# Given parameters
Fs = 40  # Sampling frequency in Hz
Ts = 1 / Fs  # Sampling period in seconds
N = 10  # First 10 samples (n = 0 to 9)

# Continuous time for smooth curve plotting
t_cont = np.linspace(0, (N - 1) * Ts, 1000)

# Sample indices and sampling times
n = np.arange(N)
t_samples = n * Ts

# Compute continuous signals
x1_cont = np.cos(20 * np.pi * t_cont)
x2_cont = np.cos(100 * np.pi * t_cont)

# Compute discrete sampled values
x1_sampled = np.cos(20 * np.pi * t_samples)
x2_sampled = np.cos(100 * np.pi * t_samples)

# Evaluate options programmatically
option_A = np.all(x1_sampled[:3] > x2_sampled[:3])
option_B = np.all(x1_sampled[-3:] > x2_sampled[-3:])
option_C = np.all(x2_sampled > x1_sampled)
option_D = np.all(np.isclose(x1_sampled[3:7], x2_sampled[3:7]))

# Print evaluation to console
print(f"(A) First three samples x1 > x2:  {option_A}")
print(f"(B) Last three samples x1 > x2:   {option_B}")
print(f"(C) All samples x2 > x1:          {option_C}")
print(f"(D) Fourth-seventh samples x1=x2: {option_D}")

# Plotting setup
fig, axs = plt.subplots(2, 1, figsize=(11, 9), sharex=True)

# Subplot 1: Signal 1 and samples
axs[0].plot(t_cont, x1_cont, label=r'$x_1(t) = \cos(20\pi t)$', color='blue', alpha=0.7)
axs[0].stem(t_samples, x1_sampled, linefmt='b-', markerfmt='bo', basefmt='r-', label='Samples ($n=0$ to $9$)')
axs[0].set_ylabel('Amplitude')
axs[0].set_title('Signal 1: $x_1(t)$ and Sampled Points')
axs[0].grid(True)
axs[0].legend(loc='upper right')

# Subplot 2: Signal 2 and samples
axs[1].plot(t_cont, x2_cont, label=r'$x_2(t) = \cos(100\pi t)$', color='orange', alpha=0.7)
axs[1].stem(t_samples, x2_sampled, linefmt='r-', markerfmt='ro', basefmt='r-', label='Samples ($n=0$ to $9$)')
axs[1].set_xlabel('Time $t$ (seconds)')
axs[1].set_ylabel('Amplitude')
axs[1].set_title('Signal 2: $x_2(t)$ and Sampled Points')
axs[1].grid(True)
axs[1].legend(loc='upper right')

# Highlight the 4th to 7th samples (indices n = 3, 4, 5, 6)
axs[1].axvspan(t_samples[3], t_samples[6], color='yellow', alpha=0.2, label='4th to 7th samples (n=3 to 6)')

# Add evaluated text onto the plot
eval_text = (
    "Option Evaluation Results:\n"
    f"(A) 1st 3 samples x1 > x2: {option_A}\n"
    f"(B) Last 3 samples x1 > x2: {option_B}\n"
    f"(C) All samples x2 > x1: {option_C}\n"
    f"(D) 4th-7th samples x1 = x2: {option_D}\n\n"
    "Correct Answer: Option (D)"
)

plt.figtext(0.15, 0.02, eval_text, fontsize=10, bbox=dict(facecolor='white', alpha=0.8, edgecolor='black'))

plt.subplots_adjust(bottom=0.22)
plt.savefig("q13.pdf")
subprocess.run(shlex.split("termux-open q13.pdf"))

