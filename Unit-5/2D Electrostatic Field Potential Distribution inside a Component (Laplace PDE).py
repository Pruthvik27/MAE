import numpy as np
import matplotlib.pyplot as plt

# Parameters
V0 = 10.0  # Top wall potential (Volts)
grid_points = 100

# Create spatial coordinate meshes
x = np.linspace(0, np.pi, grid_points)
y = np.linspace(0, np.pi, grid_points)
X, Y = np.meshgrid(x, y)

# Compute the analytical 2D Laplace field matrix
U = V0 * (np.sinh(Y) / np.sinh(np.pi)) * np.sin(X)

# Render 2D Electrostatic Potential Contour Plot
plt.figure(figsize=(7, 6))
contour = plt.contourf(X, Y, U, levels=20, cmap='plasma')
cbar = plt.colorbar(contour)
cbar.set_label('Voltage Potential Level (Volts)', rotation=270, labelpad=15)

plt.title("Steady-State 2D Voltage Field Potential Distribution $\nabla^2 u = 0$")
plt.xlabel("Component Horizontal Axis ($x$)")
plt.ylabel("Component Vertical Axis ($y$)")
plt.grid(True, alpha=0.3)
plt.show()