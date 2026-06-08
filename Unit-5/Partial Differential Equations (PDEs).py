import numpy as np
import matplotlib.pyplot as plt

# Component parameters
L = 1.0        # Width of the insulating layer
c_squared = 0.25 # Field diffusion coefficient
x_mesh = np.linspace(0, L, 200)
time_steps = [0.0, 0.1, 0.4, 1.2] # Evaluation checkpoints in seconds

plt.figure(figsize=(8, 4))

for time in time_steps:
    # Compute potential field profiles using our derived equation
    u_field = 55 * np.sin(2 * np.pi * x_mesh / L) * np.exp(-c_squared * (2 * np.pi / L)**2 * time)
    plt.plot(x_mesh, u_field, label=f'Time t = {time}s')

plt.title("Electric Field Potential Dissipation Across a Component Layer")
plt.xlabel("Layer Position Coordinates (x)")
plt.ylabel("Potential Profile u(x,t)")
plt.axhline(0, color='k', linestyle=':', alpha=0.5)
plt.grid(True, linestyle=':')
plt.legend()
plt.show()