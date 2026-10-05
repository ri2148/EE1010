import numpy as np
import matplotlib.pyplot as plt
import subprocess
import shlex
# Range of discrete time steps updated to 20
N = 20
n = np.arange(0, N + 1)

# 1. Recurrence Relation: T(n) = 2T(n-1) + n*2^n, T(0) = 1
T_rec = np.zeros(N + 1, dtype=np.int64)
T_rec[0] = 1
for i in range(1, N + 1):
    T_rec[i] = 2 * T_rec[i - 1] + i * (2**i)

# 2. Difference Equation: X(n) = 2*X(n-1)*u(n-1) + n*(2^n)*u(n) + delta(n)
X_diff = np.zeros(N + 1, dtype=np.int64)
for i in range(N + 1):
    u_i = 1 if i >= 0 else 0
    u_i_1 = 1 if (i - 1) >= 0 else 0
    delta_i = 1 if i == 0 else 0
    prev = X_diff[i - 1] if i > 0 else 0
    X_diff[i] = 2 * prev * u_i_1 + i * (2**i) * u_i + delta_i

# 3. Theoretical Closed-Form Solution: T(n) = (1 + (n^2 + n)/2) * 2^n
T_theo = (1 + (n**2 + n) // 2) * (2**n)

# --- Plotting Verification ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Subplot 1: Overlap Comparison (Log Scale)
ax1.plot(n, T_theo, 'b-', label='Theoretical Solution $T(n)$', linewidth=2)
ax1.plot(n, T_rec, 'ro', label='Recurrence Relation $T(n)=2T(n-1)+n2^n$', markersize=7, fillstyle='none')
ax1.plot(n, X_diff, 'kx', label='Difference Eq $X(n)$ with $u(n)$', markersize=7)
ax1.set_yscale('log')
ax1.set_xlabel('n', fontsize=11)
ax1.set_ylabel('Value [Log Scale]', fontsize=11)
ax1.set_title('Visual Overlap Verification ($N=20$)', fontsize=13)
ax1.grid(True, which="both", linestyle="--", alpha=0.5)
ax1.legend()

# Subplot 2: Absolute Difference (Zero Error Check)
err_rec = np.abs(T_rec - T_theo)
err_diff = np.abs(X_diff - T_theo)

ax2.plot(n, err_rec, 'r-o', label='|Recurrence - Theoretical|')
ax2.plot(n, err_diff, 'k--x', label='|Difference Eq - Theoretical|')
ax2.set_xlabel('n', fontsize=11)
ax2.set_ylabel('Absolute Error', fontsize=11)
ax2.set_title('Absolute Difference (Exact Verification)', fontsize=13)
ax2.set_ylim(-0.5, 1.0)
ax2.grid(True, linestyle="--", alpha=0.5)
ax2.legend()

plt.tight_layout()
plt.savefig("Plot.pdf")
subprocess.run(shlex.split("termux-open Plot.pdf"))
