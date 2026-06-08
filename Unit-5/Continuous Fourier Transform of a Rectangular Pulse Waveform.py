import numpy as np
import matplotlib.pyplot as plt

# Given physical constants
V0 = 5.0  # Pulse height (Volts)
a = 1.0   # Half-width (seconds)

# Continuous frequency array sweep
omega = np.linspace(-20, 20, 1000)

# Continuous analytical expression calculation
# Avoiding division by zero at omega = 0
F_omega = np.where(omega == 0, 2 * V0 * a, 2 * V0 * np.sin(omega * a) / omega)

plt.figure(figsize=(8, 4))
plt.plot(omega, F_omega, 'b-', linewidth=2, label='$F(\omega) = 2V_0\\frac{\\sin(\\omega a)}{\\omega}$')
plt.axhline(0, color='black', linestyle=':', alpha=0.5)
plt.title("Continuous Fourier Spectrum of a Single Voltage Pulse")
plt.xlabel("Angular Frequency $\omega$ (rad/s)")
plt.ylabel("Spectral Density Amplitude")
plt.grid(True, linestyle=':')
plt.legend()
plt.show()