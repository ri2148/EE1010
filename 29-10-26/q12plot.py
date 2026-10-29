import matplotlib.pyplot as plt
import numpy as np
import subprocess
import shlex

# 1. Define Point P coordinates
P = np.array([1.0, 0.0, np.sqrt(2)])

# 2. Compute Gradient Vector ∇F at P: F(x,y,z) = 2x² - y² - z²
# ∇F = [4x, -2y, -2z] -> at P(1, 0, √2): [4, 0, -2√2]
grad = np.array([4.0, 0.0, -2 * np.sqrt(2)])

# 3. Compute Magnitude (L2 Norm)
norm_grad = np.linalg.norm(grad)

# 4. Compute Unit Normal Vector n
unit_normal = grad / norm_grad

# 5. Define two tangent vectors on the surface at P to verify orthogonality
# Tangent vector 1 along x-direction: v1 = [1, 0, dz/dx] = [1, 0, √2]
# Tangent vector 2 along y-direction: v2 = [0, 1, dz/dy] = [0, 1, 0]
v1 = np.array([1.0, 0.0, np.sqrt(2)])
v2 = np.array([0.0, 1.0, 0.0])

dot_v1 = np.dot(unit_normal, v1)
dot_v2 = np.dot(unit_normal, v2)

# --- PRINT ALL REQUIRED VALUES ---
print("=" * 50)
print("COMPUTED VALUES AT POINT P(1, 0, √2)")
print("=" * 50)
print(f"Point P Coordinates     : {P}")
print(f"Gradient Vector (∇F)    : {grad}")
print(f"Magnitude ||∇F||        : {norm_grad:.6f}  (Exact: 2*sqrt(6) = {2*np.sqrt(6):.6f})")
print(f"Unit Normal Vector (n)  : {unit_normal}")
print(f"Exact Expression for n  : (√2/3)*i - (1/√3)*k  ≈ [{np.sqrt(2/3):.6f}, 0, {-1/np.sqrt(3):.6f}]")
print("-" * 50)
print("ORTHOGONALITY VERIFICATION (Dot Products with Tangents)")
print(f"n · Tangent Vector 1    : {dot_v1:.1e} (Should be 0)")
print(f"n · Tangent Vector 2    : {dot_v2:.1e} (Should be 0)")
print("=" * 50)

# --- 3D VISUALIZATION CODE ---
x = np.linspace(0.2, 1.8, 100)
y = np.linspace(-1.0, 1.0, 100)
X, Y = np.meshgrid(x, y)

Z_sq = 2 * X**2 - Y**2
Z_sq[Z_sq < 0] = np.nan
Z = np.sqrt(Z_sq)
Z_tangent = np.sqrt(2) * X

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, alpha=0.6, cmap='viridis', edgecolor='none')
ax.plot_surface(X, Y, Z_tangent, alpha=0.3, color='orange')
ax.scatter([P[0]], [P[1]], [P[2]], color='red', s=100, zorder=5)
ax.quiver(P[0], P[1], P[2], unit_normal[0], unit_normal[1], unit_normal[2], 
          color='red', length=0.8, linewidth=3, arrow_length_ratio=0.3)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(r'Surface $z^2 = 2x^2 - y^2$ and Unit Normal Vector $\vec{n}$ at $P(1, 0, \sqrt{2})$', fontsize=12)
ax.view_init(elev=20, azim=45)

plt.savefig('surface_normal_verification.png', bbox_inches='tight', dpi=150)
plt.savefig("Gradient.pdf")
subprocess.run(shlex.split("termux-open Gradient.pdf"))
