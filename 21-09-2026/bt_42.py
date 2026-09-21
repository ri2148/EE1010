import matplotlib.pyplot as plt
import numpy as np
import subprocess
import shlex
#System parameters
tau = 40.0  #Time constant in seconds
target_ratio = 0.95 

#Solve for time t analytically
t_95 = -tau * np.log(1 - target_ratio)
print(f"Time required for 95% response: {t_95:.4f} seconds")

#Generating the time domain data for plotting
t = np.linspace(0, 200, 1000)
vc_normalized = 1 - np.exp(-t / tau)

#Creating plot
plt.figure(figsize=(8, 5))
plt.plot(
    t,
    vc_normalized,
    label=r"$v_c(t)/V_0 = 1 - e^{-t/40}$",
    color="blue",
    linewidth=2,
)

#Highlighting the 95% threshold point
plt.scatter(
    [t_95],
    [target_ratio],
    color="red",
    zorder=5,
    s=50,
    label=f"95% Target (t ≈ {t_95:.2f} s)",
)
plt.axhline(y=target_ratio, color="r", linestyle="--", alpha=0.7)
plt.axvline(x=t_95, color="r", linestyle="--", alpha=0.7)

# Formatting
plt.title("RC Circuit First-Order Step Response", fontsize=14)
plt.xlabel("Time $t$ (seconds)", fontsize=12)
plt.ylabel("Normalized Voltage $v_c(t) / V_0$", fontsize=12)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(fontsize=11)
plt.xlim(0, 200)
plt.ylim(0, 1.1)

plt.tight_layout()
plt.savefig("BT-42.pdf")
subprocess.run(shlex.split("termux-open BT-42.pdf"))
