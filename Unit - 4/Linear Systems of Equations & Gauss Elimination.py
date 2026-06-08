import numpy as np
import scipy.linalg as la

# Define Matrix A and vector b
A = np.array([[2.0, 1.0, -1.0],
              [4.0, 4.0, -1.0],
              [-2.0, 3.0, 4.0]])

b = np.array([1.0, -2.0, 3.0])

# Direct High-Precision Numerical Solve
x = la.solve(A, b)

print("--- Gauss Elimination Verification ---")
print(f"Loop Variable x1: {x[0]:.2f}")
print(f"Loop Variable x2: {x[1]:.2f}")
print(f"Loop Variable x3: {x[2]:.2f}\n")

# Verify identity Ax = b
print("Verification Matrix product (Ax):", A.dot(x))