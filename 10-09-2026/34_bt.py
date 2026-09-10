#code by Arjun
#date:10-09-2026
#using gauss elimination
import numpy as np

#Defining initial augmented matrix tracking coefficients: [x, y, constant, k_coeff]
#Row 1: 2x + 3y = 6  -> [2, 3, 6, 0]
#Row 2: 4x + 6y = 3k -> [4, 6, 0, 3]
matrix = np.array([
    [2.0, 3.0, 6.0, 0.0],
    [4.0, 6.0, 0.0, 3.0]
])

#Row Operation: R2 -> R2 - 2*R1
matrix[1] = matrix[1] - 2 * matrix[0]

#Display transformed matrix
print("Matrix after operation (R2 -> R2 - 2*R1):")
print(f"[{matrix[0, 0]:.0f}  {matrix[0, 1]:.0f} :  {matrix[0, 2]:.0f}]")
print(f"[{matrix[1, 0]:.0f}  {matrix[1, 1]:.0f} :  3k - 12]\n")

#Solve for infinite solutions: 3k - 12 = 0
const_term = matrix[1, 2]  # -12.0
k_coeff = matrix[1, 3]     # 3.0

#3k - 12 = 0  =>  3k = 12  =>  k = 12 / 3
k = -const_term / k_coeff

print(f"For infinite solutions:")
print(f"{k_coeff:.0f}k - {abs(const_term):.0f} = 0")
print(f"{k_coeff:.0f}k = {abs(const_term):.0f}")
print(f"k = {int(k)}")

