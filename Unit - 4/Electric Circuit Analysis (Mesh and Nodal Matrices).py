import numpy as np

# R matrix mapping self and mutual network loop resistances
R = np.array([[6.0, -4.0],
              [-4.0, 5.0]])

# Source vector V
V = np.array([10.0, -5.0])

# Compute using matrix inverse calculation internal functions
I = np.linalg.solve(R, V)

print("--- Automated Circuit Matrix Mesh Solver ---")
print(f"Calculated Loop Current I1 = {I[0]:.3f} Amperes")
print(f"Calculated Loop Current I2 = {I[1]:.3f} Amperes")

# Compute power delivered by the primary 10V source: P = V * I1
power_10v = 10.0 * I[0]
print(f"Total Power Dissipation Draw from 10V source = {power_10v:.2f} Watts")